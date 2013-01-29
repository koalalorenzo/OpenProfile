#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-
from datetime import datetime
from openprofile.objects.Profile import Profile

class Connection(object):
    """
        This object manage the "connections" between two
        OpenProfile installations. 
    """
    def __init__(self):
        self.username = ""
        self.userhash = ""
        
        self.blocked = False
        self.group_id = ""
        
        self.last_time_updated = datetime.now()
        self.connected_since = datetime.now()
        
        self.database = None
        
    def get_user_profile(self, profile_url):
        """ This command get the Profile of this connection and save it in the database """
        profile = Profile()
        profile.database = self.database
        profile.profile_url = profile_url
        profile.get_profile_from_remote()
        profile.save()
        
        self.last_time_updated = datetime.now()
        if not self.userhash:
            self.userhash = profile.userhash
        return profile
        
    def by_dictionary(self, dictionary):
        self.profile_url = dictionary['profile_url']
        self.username = dictionary['username']
        self.password = dictionary['password']
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
        old['password'] = self.password
        old['userhash'] = self.userhash
        old['avatar'] = self.avatar
        
        old['first_name'] = self.first_name
        old['second_name'] = self.second_name 
        
        old['emails'] = self.emails
        old['phones'] = self.phones
        
        old['twitter'] = self.twitter
        old['facebook'] = self.facebook
        
        old['description'] = self.description
        old['short_description'] = self.short_description
        old['keywords'] = self.keywords
        
        old['is_admin'] = self.is_admin
        
        return old
