from instagrapi import Client 
from dotenv import load_dotenv
import os 
import logging 
load_dotenv()

class AuthUser:
    def __init__(self):
        self._username = os.getenv("IG_USERNAME")
        self._password = os.getenv("IG_PASSWORD") 
        self.insta = Client()                        #why in paramter
   

    def login(self):
        self.insta.login(self._username, self._password) 
        self.insta.dump_settings("session.json")         #adds json to session.json
        print("logged in && saved session")
        return self.insta      #returns logged in session 
    

    def load_session(self):
        self.insta.load_settings("session.json")   # reads from file session.json
        self.insta.login(self._username, self._password)
        return self.insta






