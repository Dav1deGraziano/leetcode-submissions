class User:

    def __init__(self):
        self.tweets = []
        self.n_tweets = 0
        self.follows = set()

class Twitter:

    def __init__(self):
        self.users = {}
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        if str(userId) not in self.users:
            self.users[str(userId)] = User()
        self.users[str(userId)].tweets.append([self.timestamp,tweetId])
        self.users[str(userId)].n_tweets += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.users[str(userId)]
        if user.n_tweets <= 10:
            queue = [x for x in user.tweets]
            len_queue = user.n_tweets
        else:
            queue = [x for x in user.tweets[-1:-11:-1]]
            len_queue = 10
        if user.follows:
            for followee in user.follows:
                followee = self.users[followee]
                if followee.n_tweets <= 10:
                    queue.extend(followee.tweets)
                    len_queue += followee.n_tweets
                else:
                    queue.extend(followee.tweets[-1:-11:-1])
                    len_queue += 10
        queue.sort(key=lambda x:x[0],reverse = True)
        res = [int(queue[i][1]) for i in range(min(10,len_queue))]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if str(followerId) not in self.users:
                self.users[str(followerId)] = User()
            if str(followeeId) not in self.users:
                self.users[str(followeeId)] = User()
            self.users[str(followerId)].follows.add(str(followeeId))
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if str(followerId) in self.users and str(followeeId) in self.users[str(followerId)].follows:
            self.users[str(followerId)].follows.discard(str(followeeId))
        
