from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.posts = defaultdict(list)
        self.timestamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.timestamp, tweetId))
        self.timestamp += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        allTweets = set(self.posts[userId][-10:])
        for i in self.followees[userId]:
            allTweets.update(self.posts[i][-10:])
        return list(map(lambda x: x[1], sorted(allTweets, reverse=True)[:10]))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)

