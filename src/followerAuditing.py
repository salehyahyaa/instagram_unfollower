from instagrapi import Client
from database.connection import Connection

class FollowerAuditing:
    def __init__(self, client): 
        self.client = client        #hows this the same instance as authUser class's clinet?
        self.user_id = client.user_id 

    
    def get_followers(self):
        followers =  self.client.user_followers(self.user_id)
        return [user.username for user in followers.values()]
    
    
    def get_following(self): 
        following = self.client.user_following(self.user_id)
        return [user.username for user in following.values()]
    

    def audit_unfollows(self): 
        todays_followers = set(self.get_followers())              #store it in hashset for O(1) lookup insted of an array causing O(n) lookup
        todays_following = set(self.get_following())
        todays_mutuals = todays_followers & todays_following

        yesterdays_mutals = set(Connection.get_yesterday_mutuals())

        unfollowed =  yesterdays_mutals - todays_mutuals

        for user in unfollowed:                                   #auto unfollows
            user_id = self.client.user_id_from_username(user)
            self.client.user_unfollow(user_id)

                                                                  # save todays snapshot to db
        Connection.save_snapshot(list(todays_followers), 'follower')
        Connection.save_snapshot(list(todays_following), 'following')
        Connection.save_snapshot(list(todays_mutuals), 'mutual')

        return unfollowed
        

    

















    #custom insta logic to check daily if followees still follow if not unfollow 
