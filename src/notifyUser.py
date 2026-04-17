import instagrapi 
from followerAuditing import FollowerAuditing


class NotifyUser: 

    def notify(unfollowed):
        for user in unfollowed: 
            os.system(f"osascript -e 'display notification \"{user} unfollowed you\" with title \"Instagram Auditor\"'")
