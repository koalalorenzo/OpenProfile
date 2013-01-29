#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-
from datetime import datetime
from hashlib import sha1

from pbkdf2 import crypt, PBKDF2
from Crypto.Cipher import AES

class Message(object):
    def __init__(self, url):
                
        self.author = "" # profile_url
        self.receiver = "" # profile_url
                
        self.content = "" # Encrypted message
        self.content_hash = "" # sha1 hash to verify the message
        self.keywords = list()
        self.created_at = datetime.now()
                         
        self.database = None
        
    def encrypt_content(self, secret):
        if self.content:
            raise Exception("Content already crypted")

        self.__cipher = AES.new(secret)
        content = self.content.encode("base64")
        while not len(content)%16 == 0:
            content = " " + content
        self.content = self.__cipher.encrypt(content).encode("base64")
        return self.content
     
    def decrypted_content(self, secret):
        if not self.content:
            raise Exception("No content found")
        self.__cipher = AES.new(secret)    
        content = self.__cipher.decrypt(self.content.decode("base64"))
        return content.decode("base64")
                
    def by_dictionary(self, dictionary):
        self.url = dictionary['url']
        self.author = dictionary['author']
        self.title = dictionary['title']
        self.content = dictionary['content']
        self.keywords = dictionary['keywords']
        self.created_at = dictionary['created_at']
        
    def load(self):
        search = self.database.messages.find_one({"url": self.url})
        if not search:
            raise Exception("Page not found")
        self.by_dictionary(search)
        return
    
    def save(self):
        self.__crypt_password()
        search = self.database.messages.find_one({"url": self.url})
        dictionary = self.__dict__(old=search)
        self.database.users.save(dictionary)

        return
        
    def __dict__(self, old=None):
        if not old:
            old = dict()
        
        old['url'] = self.url
        old['author'] = self.author
        old['title'] = self.title
        old['content'] = self.content
        old['keywords'] = self.keywords
        old['created_at'] = self.created_at
        
        return old
