#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from hashlib import sha1
from datetime import datetime
import requests

class AdminNotFound(Exception):
    pass
    
class Profile(object):
    """ 
        The Profile Object is the basic entity of the entire System because it
        manage authentication, security and provides informations about 
        other profiles.
    """
    def __init__(self):
        self.profile_url = ""
        
        self.username = ""
        self.userhash = ""
        
        self.avatar = "" # URL avatar
        
        self.first_name = ""
        self.second_name = ""
        self.complete_name = ""
        
        self.emails = list() 
        self.phones = list() 
        
        self.description = ""
        self.short_description = "" # 140 chars ( better if 119 to insert the URL of your profile )
        
        self.social_networks = list() # {"social":"twitter", "link":"http://twitter.com/koalalorenzo" }
        self.keywords = list()
        
        self.is_admin = False
        self.database = None
        
    def get_profile_from_remote(self, profile_url=None):
        """ Load and return the user profile from a remote installation """
        if not profile_url:
            profile_url = self.profile_url
        if profile_url[-1] == "/":
            profile_url = profile_url[0:-1] 
        r = requests.get("%s/api/profile/owner" % profile_url)    
        self.by_dictionary(r.json, avoid_admin=False)
        return self
        
    def set_userhash(self, password):
        self.userhash = sha1("%s-%s" % ( self.username, password )).hexdigest()
        return self.userhash
        
    def verify_login(self, username, password):
        check_userhash = sha1("%s-%s" % ( username, password )).hexdigest()
        if self.userhash != check_userhash:
            return False
        return True
        
    def load_admin(self):
        search = self.database.users.find_one({"is_admin":True})
        if not search:
            raise AdminNotFound()
        self.by_dictionary(search)
        
    def already_exist(self):
        search = self.database.users.find_one({"userhash": self.userhash})
        if search:
            return True
        return False
        
    def by_dictionary(self, dictionary, avoid_admin=False):
        self.profile_url = dictionary['profile_url']
        self.username = dictionary['username']
        self.userhash = dictionary['userhash']
        
        self.first_name = dictionary['first_name']
        self.second_name = dictionary['second_name']
        self.complete_name = dictionary['complete_name']
        
        self.emails = dictionary['emails']
        self.phones = dictionary['phones']
 
        self.description = dictionary['description']
        self.short_description = dictionary['short_description']
        self.keywords = dictionary['keywords']

        if not avoid_admin:
            self.is_admin = dictionary['is_admin']
        
    def load(self):
        search = self.database.users.find_one({"userhash": self.userhash})
        if not search:
            raise Exception("Username not found")
        self.by_dictionary(search)
    
    def save(self):
        search = self.database.users.find_one({"userhash": self.userhash})
        dictionary = self.__dict__(old=search)
        self.database.users.save(dictionary)
        
    def __dict__(self, old=None):
        if not old:
            old = dict()
        
        old['profile_url'] = self.profile_url
        old['username'] = self.username
        old['userhash'] = self.userhash
        old['avatar'] = self.avatar
        
        old['first_name'] = self.first_name
        old['second_name'] = self.second_name 
        old['complete_name'] = self.complete_name
        
        old['emails'] = self.emails
        old['phones'] = self.phones
        
        old['description'] = self.description
        old['short_description'] = self.short_description
        
        old['social_networks'] = self.social_networks
        old['keywords'] = self.keywords
        
        old['is_admin'] = self.is_admin
        
        return old
        
