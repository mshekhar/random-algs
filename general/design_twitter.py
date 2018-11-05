import collections
import heapq
import itertools


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweet_timer = itertools.count(step=-1)
        self.user_tweets_list = collections.defaultdict(collections.deque)
        self.follower_set = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.user_tweets_list[userId].appendleft((next(self.tweet_timer), tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed
        must be posted by users who the user followed or by the user herself. Tweets must be ordered
        from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        for u in self.follower_set.get(userId, set()) | {userId}:
            print self.user_tweets_list.get(u, [])
        sorted_tweets = heapq.merge(*(self.user_tweets_list.get(u, [])
                                      for u in self.follower_set.get(userId, set()) | {userId}))
        return [t for _, t in itertools.islice(sorted_tweets, 10)]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.follower_set[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.follower_set[followerId].discard(followeeId)

    @classmethod
    def generic_runner(cls, oper, val, expected):
        obj = Twitter()
        c = 1
        for op, v in zip(oper[1:], val[1:]):
            res = getattr(obj, op)(*v)
            print op, v[0], expected[c], res, expected[c] == res
            c += 1


null = None
# Twitter.generic_runner(
#     ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"],
#     [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]], [null, null, [5], null, null, [6, 5], null, [5]])

# Twitter.generic_runner(["Twitter", "postTweet", "unfollow", "getNewsFeed"],
#                        [[], [1, 5], [1, 1], [1]],
#                        [None, True, True, True])

Twitter.generic_runner(["Twitter", "postTweet", "postTweet", "getNewsFeed"],
                       [[], [1, 5], [1, 3], [1]],
                       [null, null, null, [3, 5]])

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
