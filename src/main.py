import instagrapi
import schedule
import time 
import os 
from authUser import AuthUser
from followerAuditing import FollowerAuditing
from notifyUser import NotifyUser


def run(): 
    authUser = AuthUser() 
    client = authUser.get_client()
    audit = FollowerAuditing(client)            
    unfollowed = audit.audit_unfollows()
    NotifyUser().notify(unfollowed)


#schedule.every().day.at("18:30").do(run)        # runs once a day at 6:30pm

while True:
    schedule.run_pending()
    time.sleep(60)                              # check every minute if it's time to run