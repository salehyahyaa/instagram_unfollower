import instagrapi 
from followerAuditing import FollowerAuditing
import os


class NotifyUser: 

    def notify(unfollowed):
        for user in unfollowed: 
            os.system(f"osascript -e 'display notification \"{user} unfollowed you\" with title \"Instagram Auditor\"'")
