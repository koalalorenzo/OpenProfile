#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from hashlib import sha1
from datetime import datetime

class Profile(object):
    def __init__(self):
        self.profile_url = ""
        
        self.username = ""
        self.password = None
        self.__crptd = False
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
        
    def change_password(self, new_password):
        if self.__crptd:
            self.password = sha1(new_password).hexdigest()
        else:
            self.password = new_password
        
    def __crypt_password(self):
        if not self.password: return
        if self.__crptd: return
        self.password = sha1(self.password).hexdigest()
        self.__crptd = True
        
    def verify_login(self, username, password):
        if self.__crptd:
            check = sha1(password).hexdigest()
        else: 
            check = password
        if self.password != check:
            return False
        return True

        
    def already_exist(self):
        search = self.database.users.find_one({"userhash": self.userhash})
        if search:
            return True
        return False
        
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
        
    def load(self, username):
        search = self.database.users.find_one({"userhash": self.userhash})
        if not search:
            raise Exception("Username not found")

        return
    
    def save(self):
        self.__crypt_password()
        search = self.database.users.find_one({"userhash": self.userhash})
        dictionary = self.__dict__(old=search)
        self.database.users.save(dictionary)

        return
        
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
        
