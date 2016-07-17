__author__ = 'sharvija'
from models import AutoFollow, SearchResult, TwitterSecret
import util
import api, uuid

class SearchController:
    def __init__(self, h, query, lastUsedId=0):
        self.handler = h
        self.query=query
        self.lastUsedId=lastUsedId

    def nextTweet(self):
        if self.lastUsedId <1:
            print "last used id is not valid returning first one"
            return self.findFirstTweet()
        print "last used-id: "+str(self.lastUsedId)
        res=SearchResult.objects.filter(query=self.query, tweetId__gt=self.lastUsedId).order_by('tweetId')[:1]
        if len(res) == 0:
            return None
        print "returning "+str(res[0].tweetId)
        return res[0]

    def findFirstTweet(self):
        res=SearchResult.objects.filter(query=self.query).order_by('tweetId')[:1]
        if len(res) == 0:
            return None
        return res[0]

    def findLastTweet(self):
        res=SearchResult.objects.filter(query=self.query).order_by('-tweetId')[:1]
        if len(res) == 0:
            return None
        return res[0]


    def searchOnTwitter(self):
        search = api.Searching()
        d=search.search(self.handler, self.query, maxTweets=100, sinceId=self.lastUsedId)
        return d.get('tweetCount')

    def getOneTweet(self):
        tweet = self.nextTweet()
        if tweet is None:
            self.searchOnTwitter()
            tweet=self.nextTweet()
        if tweet is None:
            raise util.NoSearchResultFound(detail="No new tweet found, although searched on twitter")
        return tweet


class AutoFollowController:

    def __init__(self, handler, query):
        self.h = handler
        self.q = query

    def followByTweet(self):
        objs = AutoFollow.objects.filter(handler=self.h, query=self.q, status='following').order_by(
            '-tweetId')[:1]
        tweet=None
        if len(objs)<1:
            lastTweetId = 0
        else:
            tweet = objs[0]
            lastTweetId = tweet.tweetId
        print "last followed tweetId: "+str(lastTweetId)
        alreadyFollow = True
        while alreadyFollow:
            sc = SearchController(self.h, self.q, lastTweetId)
            tweet = sc.getOneTweet()
            user = tweet.screenName
            lastTweetId = tweet.tweetId
            alreadyFollow = self.doIAutoFollow(user)
        try:
            afObj= self.constructAFObj(tweet)
            print "about to add new"
            afObj.save()
            print "added as a new"
            wrap=api.TW_API.get(self.h)
            wrap.followUserByScreenName(tweet.screenName)
            afObj.status="following"
            afObj.save()
        except Exception as e:
            print "an err while following"+str(e.message)
            raise e
        return {"tweetId":lastTweetId, "following":tweet.screenName, "query":self.q, "handler":self.h}

    def constructAFObj(self, tweet):
        af = AutoFollow()
        af.tweetId = tweet.tweetId
        af.screenName = tweet.screenName
        af.userId = tweet.userId
        af.query = self.q
        secret = TwitterSecret.objects.get(handler = self.h)
        af.handler = secret
        af.uuid = uuid.uuid4()
        af.status="new"
        return af

    def doIAutoFollow(self, screenName):
        f=True
        try:
            obj = AutoFollow.objects.get(handler=self.h, screenName = screenName, status = 'following')
        except AutoFollow.DoesNotExist:
            f=False
        return f

    def clearFollowing(self, retain):
        print("In clearFollowing(), retain: "+str(retain))
        if type(retain) is not int:
            raise util.InvalidValueType(detail="'retain' value must be Integer!")
        total= AutoFollow.objects.filter(handler=self.h, status = 'following').count()
        print("total auto following is "+str(total))
        toUnfollow= total-retain
        unfollow=[]
        if toUnfollow>0:
            listToUnFollow=AutoFollow.objects.filter(handler=self.h, status = 'following')[:toUnfollow]

            for af in listToUnFollow:
                try:
                    wrapper= api.TW_API.get(self.h)
                    wrapper.unFollowByScreenName(af.screenName)
                    af.status="unfollowed"
                    af.save()
                    unfollow.append(af.screenName)
                except Exception:
                    pass
        return {"unfollwed":unfollow,"totalUnfollowed": toUnfollow}


    def clearAllAutoFollow(self):
        listToUnFollow=AutoFollow.objects.filter(handler=self.h, status = 'following')
        for af in listToUnFollow:
            wrapper= api.TW_API.get(self.h)
            wrapper.unFollowByScreenName(af.screenName)
            af.status="unfollowed"
            af.save()
