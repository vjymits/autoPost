__author__ = 'sharvija'
import tweepy
import threading
import time
from util import TwitterError, TwitterRateLimitExceed

class TwitterWrapper():
    twApi = None
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            self.twApi= tweepy.API(auth)
        except tweepy.RateLimitError as e:
            raise TwitterRateLimitExceed()
        except tweepy.TweepError as e:
            raise TwitterError(msg=e.message)


    def postTweet(self, tweetStr):
        try:
            status = self.twApi.update_status(status=tweetStr)
        except tweepy.RateLimitError:
            raise TwitterRateLimitExceed()
        except tweepy.TweepError as e:
            raise TwitterError(msg=e.message)
        return status

    def replyTweet(self, text, user, tweetId):
        try:
            m = "@%s " %(user)+text
            self.twApi.update_status(m, tweetId)
        except tweepy.RateLimitError as e:
            raise TwitterRateLimitExceed()
        except tweepy.TweepError as e:
            raise TwitterError(msg=e.message)
        return m


    def getTrends(self, woid ):
        try:
            js=self.twApi.trends_place(woid)
        except tweepy.RateLimitError as e:
            raise TwitterRateLimitExceed()
        except tweepy.TweepError as e:
            raise TwitterError(msg=e.message)
        return js

    def getApi(self):
        return self.twApi

    def search(self, query, maxTweets):
        try:
            searched_tweets = [status for status in tweepy.Cursor(self.twApi.search, q=query).items(maxTweets)]
        except tweepy.RateLimitError as e:
            raise TwitterRateLimitExceed()
        except tweepy.TweepError as e:
            raise TwitterError(msg=e.message)
        return searched_tweets

class TweetThread(threading.Thread):

    def __init__(self, twWrap, tweetList=[], wait=0):
        threading.Thread.__init__(self)
        self.tweets = tweetList
        self.wait= wait
        self.twWrapper = twWrap

    def addTweet(self, tw_str):
        self.tweets.append(tw_str)

    def run(self):
        for t in self.tweets:
            time.sleep(self.wait)
            self.twWrapper.postTweet(t)









