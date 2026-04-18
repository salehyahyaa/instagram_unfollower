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
   

    def get_client(self):
        try:
            self.insta.load_settings("session.json")
            self.insta.get_timeline_feed()                   # validates session
            print("Session loaded")
        except:
            print("Session invalid → logging in once")            
            self.insta.login(self._username, self._password)
            self.insta.dump_settings("session.json")

        return self.insta    

    def load_session(self):
        self.insta.load_settings("session.json")   # reads from file session.json
        self.insta.login(self._username, self._password)
        return self.insta






