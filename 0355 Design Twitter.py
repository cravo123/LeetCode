import heapq

# Solution 1, decoupling
# Separate User as a new class

class User:
    def __init__(self, user_id):
        self.uid = user_id
        self.tweets = []
        self.following = set([user_id])
    
    def post_tweet(self, tweetId):
        self.tweets.append(tweetId)
    
    def follow(self, followeeId):
        self.following.add(followeeId)
    
    def unfollow(self, followeeId):
        if followeeId != self.uid: # got-cha, cannot unfollow himself
            self.following.discard(followeeId)
    
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.tid_map = {} # got-cha, tweetId doesn't mean order...
        self.idx = 0
        
    def _add_new_user(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self._add_new_user(userId)
        
        curr = self.users[userId]
        curr.post_tweet(tweetId)
        self.tid_map[tweetId] = self.idx
        self.idx -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. 
        Each item in the news feed must be posted by users 
        who the user followed or by the user herself. 
        Tweets must be ordered from most recent to least recent.
        """
        self._add_new_user(userId)
        curr = self.users[userId]
        
        q = []
        for uid in curr.following:
            p = self.users[uid]
            if p.tweets:
                q.append([self.tid_map[p.tweets[-1]], p.tweets[-1], len(p.tweets) - 1, p.tweets])
        
        res = []
        heapq.heapify(q)
        
        while q and len(res) < 10:
            _, tid, idx, t_list = heapq.heappop(q)
            res.append(tid)
            if idx > 0:
                idx -= 1
                heapq.heappush(q, [self.tid_map[t_list[idx]], t_list[idx], idx, t_list])
        
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self._add_new_user(followerId)
        self._add_new_user(followeeId)
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self._add_new_user(followerId)
        self._add_new_user(followeeId)
        self.users[followerId].unfollow(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)