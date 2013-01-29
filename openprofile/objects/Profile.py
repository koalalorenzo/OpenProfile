#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from hashlib import sha1
from datetime import datetime

class Profile(object):
    def __init__(self):
        self.profile_url = ""
        
        self.username = ""
        self.userhash = "" # sha1("%s-%s" % ( self.username, self.password ).hexdigest()
        
        self.avatar = "" # URL avatar
        
        self.first_name = ""
        self.second_name = ""
        
        self.emails = list() # Ex: "lorenzo.setale@gmail.com","koalalorenzo@gmail.com"
        self.phones = list() # Ex: "+39 329 06 84 001","+39 06 929 58 369"
        
        self.description = ""
        self.short_description = "" # 140 chars ( better if 119 to insert the URL of your profile )
                
        self.social_networks = list() # {"social":"twitter", "link":"http://twitter.com/koalalorenzo" }
        self.keywords = list()
                         
        self.is_admin = False
        self.database = None
        
    def get_userhash(self, password):
        self.userhash = sha1("%s-%s" % ( self.username, password ).hexdigest()
        return self.userhash
        
    def verify_login(self, username, password):
        check_userhash = sha1("%s-%s" % ( self.username, password ).hexdigest()
        if self.userhash != check_userhash:
            return False
        return True
        
    def load_admin(self):
        search = self.database.users.find_one({"userhash": self.userhash, "is_admin":True})
        if not search:
            raise Exception("Admin not found")
        self.by_dictionary(search)
        
    def already_exist(self):
        search = self.database.users.find_one({"userhash": self.userhash})
        if search:
            return True
        return False
        
    def by_dictionary(self, dictionary):
        self.profile_url = dictionary['profile_url']
        self.username = dictionary['username']
        self.__crptd = True
        self.userhash = dictionary['userhash']
        
        self.first_name = dictionary['first_name']
        self.second_name = dictionary['second_name']
        
        self.emails = dictionary['emails']
        self.phones = dictionary['phones']
 
        self.description = dictionary['description']
        self.short_description = dictionary['short_description']
        self.keywords = dictionary['keywords']
        
        self.is_admin = dictionary['is_admin']
        
    def load(self):
        search = self.database.users.find_one({"userhash": self.userhash})
        if not search:
            raise Exception("Username not found")
        self.by_dictionary(search)
    
    def save(self):
        self.__crypt_password()
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
        
        old['emails'] = self.emails
        old['phones'] = self.phones
        
        old['description'] = self.description
        old['short_description'] = self.short_description
        
        old['social_networks'] = self.social_networks
        old['keywords'] = self.keywords
        
        old['is_admin'] = self.is_admin
        
        return old
        
