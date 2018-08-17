import heapq


class FeedObject(object):
    def __init__(self):
        self.tweet_counter = None
        self.tweetId = None
        self.userId = None

    def __cmp__(self, other):
        return cmp(self.tweet_counter, other.tweet_counter)

    def __str__(self):
        return str(self.tweet_counter) + "_" + str(self.tweetId) + "_" + str(self.userId)

    def __repr__(self):
        return str(self.tweet_counter) + "_" + str(self.tweetId) + "_" + str(self.userId)


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_tweets = {}
        self.followee_graph = {}
        self.tweet_counter = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweet_counter -= 1
        feed_obj = FeedObject()
        feed_obj.tweet_counter = self.tweet_counter
        feed_obj.tweetId = tweetId
        feed_obj.userId = userId

        heapq.heappush(self.user_tweets.setdefault(userId, []), feed_obj)

        for followee in self.followee_graph.get(userId, set()):
            heapq.heappush(self.user_tweets.setdefault(followee, []), feed_obj)
        # print self.user_tweets.get(userId, [])

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        top_ten_tweets = []
        user_tweet_heap = self.user_tweets.get(userId, [])
        for i in range(10):
            if user_tweet_heap:
                top_ten_tweets.append(heapq.heappop(user_tweet_heap))

        for feed_obj in top_ten_tweets:
            heapq.heappush(self.user_tweets.setdefault(userId, []), feed_obj)

        # print self.user_tweets.setdefault(userId, []), top_ten_tweets
        return map(lambda feed_obj: feed_obj.tweetId, user_tweet_heap)

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId or followerId in self.followee_graph.get(followeeId, set()):
            return
        self.followee_graph.setdefault(followeeId, set()).add(followerId)
        user_tweet = self.user_tweets.setdefault(followerId, [])
        for feed_obj in self.user_tweets.get(followeeId, []):
            heapq.heappush(user_tweet, feed_obj)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId or followerId not in self.followee_graph.get(followeeId, set()):
            return
        self.followee_graph.setdefault(followeeId, set()).remove(followerId)
        new_heap = []
        for feed_obj in self.user_tweets.get(followerId, []):
            if feed_obj.userId != followeeId:
                heapq.heappush(new_heap, feed_obj)
        self.user_tweets[followerId] = new_heap


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

def generic_runner(oper, val, expected):
    twitter = Twitter()
    c = 1
    for op, v in zip(oper[1:], val[1:]):
        res = getattr(twitter, op)(*v)
        print op, v, expected[c], res
        c += 1
    # print twitter.user_tweets
    # print twitter.followee_graph


generic_runner(
    [
        "Twitter", "postTweet", "postTweet", "postTweet", "postTweet",
        "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
        "postTweet", "postTweet", "postTweet", "follow", "follow", "follow", "follow", "follow",
        "follow", "follow", "follow", "follow", "follow", "follow", "follow", "getNewsFeed",
        "getNewsFeed", "getNewsFeed", "getNewsFeed", "getNewsFeed"
    ],
    [
        [], [1, 6765], [5, 671], [3, 2868], [4, 8148], [4, 386], [3, 6673], [3, 7946], [3, 1445],
        [4, 4822], [1, 3781], [4, 9038], [1, 9643], [3, 5917], [2, 8847], [1, 3], [1, 4], [4, 2],
        [4, 1], [3, 2], [3, 5], [3, 1], [2, 3], [2, 1], [2, 5], [5, 1], [5, 2], [1], [2], [3], [4], [5]
    ],
    [
        None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None,
        [5917, 9643, 9038, 3781, 4822, 1445, 7946, 6673, 386, 8148],
        [8847, 5917, 9643, 3781, 1445, 7946, 6673, 2868, 671, 6765],
        [8847, 5917, 9643, 3781, 1445, 7946, 6673, 2868, 671, 6765],
        [8847, 9643, 9038, 3781, 4822, 386, 8148, 6765], [8847, 9643, 3781, 671, 6765]
    ]
)
