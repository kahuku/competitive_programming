from collections import defaultdict

class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        return [tweetId for tweetId, tweeterId in self.tweets[::-1] if tweeterId == userId or tweeterId in self.following[userId]][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.following[followerId] and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


from collections import defaultdict

class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = []
        self.cache = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))
        self.cache = defaultdict(list)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.cache:
            return self.cache[userId]

        feed = []
        for i in range(len(self.tweets) - 1, -1, -1):
            if self.tweets[i][1] in self.following[userId] or self.tweets[i][1] == userId:
                feed.append(self.tweets[i][0])
        self.cache[userId] = feed[:10]
        return feed[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        self.cache = defaultdict(list)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.following[followerId] and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
            self.cache = defaultdict(list)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)