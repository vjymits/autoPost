__author__ = 'sharvija'
import tweepy
import threading
import time

class TwitterWrapper():
    twApi = None
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.twApi= tweepy.API(auth)

    def postTweet(self, tweetStr):
        status = self.twApi.update_status(status=tweetStr)
        return status

    def getTrends(self, woid ):
        js=self.twApi.trends_place(woid)
        return js

    def getApi(self):
        return self.twApi

    def search(self, query, maxTweets):
        searched_tweets = [status for status in tweepy.Cursor(self.twApi.search, q=query).items(maxTweets)]
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









