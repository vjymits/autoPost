__author__ = 'sharvija'
import twitter
from models import TwitterSecret, Tweet, TwitterTrend, Location, SearchResult
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import serializers
import uuid
import util, const

TW_API = {}


def fill_tw_api():
    secrets = TwitterSecret.objects.all()
    for one in secrets:
        handler= one.handler
        if TW_API.get(handler, None) is None:
             wrapper = twitter.TwitterWrapper(one.consumerKey, one.consumerSecret, one.accessToken,
                                   one.accessTokenSecret)

             TW_API[handler] = wrapper

class TrendController():
    def getTrends(self, handler):
        twitterSecret = TwitterSecret.get(handler = handler)

class TweetSrl(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('text', 'img', 'handler', )

class TweetList(generics.ListAPIView):
    def post(self, request):
        data = request.data
        input = data.keys()
        allowed = ['text', 'img', 'handler', 'include', 'reply']
        mandatory = ['handler']
        include = data.get('include', None)
        reply = data.get('reply', None)
        util.validate_mandatory_params(mandatory, input)
        util.validate_allowed_params(allowed, input)
        return TweetApi().tweet(include, reply, data)

    def get(self, request):
        print "calling get()"
        api = TrendsApi()
        api.fill_trends()
        wrap = TW_API.get('@tradStrat', None)
        print str(wrap)
        return Response(wrap.getTrends(1))

    def get_queryset(self):
        print "qq"
        return "bb"

class Includable:
    allowed = ['trends', 'users']
    includeDict= None
    trends=""
    users=""
    def __init__(self, includeData):
        self.includeDict = includeData
        self.trends=self.getTrends()
        self.users=self.getUsers()

    def getUsers(self):
        valid = ['UserInSearchQuery', 'noOfUsers']
        return ""

    def getTrends(self):
        tr_str=""
        trendDict = self.includeDict.get('trends', None)
        for trend in trendDict:
            valid = ['placeId', 'rank']
            self.trends = ""
            if None:
                return self.trends
            print "trend:"+str(trend)
            util.validate_allowed_params(valid, trend.keys())
            placeId= trend.get('placeId', 1)
            rank= trend.get('rank', 1)
            tr = TwitterTrend.objects.get(location=placeId, rank=rank)
            tr_str=tr_str+' '+tr.name
        return tr_str

    def __str__(self):
        str = self.getTrends()+" "+self.users
        return str

class TrendsApi:
    def fill_trends(self):
        all = Location.objects.all()
        for one in all:
            print "location: "+str(one.placeId)
            self.updateTrendsInDB(one.placeId)
        return Response({"all trends updated"})

    def updateTrendsInDB(self, placeId):
        try:
            wrap = TW_API.get(const.DEFAULT_HANDLER, None)
            res= wrap.getTrends(placeId)
            #data= json.loads(res)
            print (str(res))
            trends = res[0].get('trends', None)
            print("trends: "+str(trends))
            if trends is None:
                return
            TwitterTrend.objects.filter(location=placeId).delete()
            i = 1
            for trend in trends:
                try:
                    tr = TwitterTrend()
                    tr.location = placeId
                    tr.name = trend.get('name')
                    tr.tweetVolume=trend.get('tweet_volume')
                    tr.rank = i
                    i=i+1
                    print "location: "+str(tr.location)
                    #print "name of trend "+str(tr.name)
                    print "rank: "+str(tr.rank)
                    tr.save()
                except Exception as e:
                    print "skip err "+str(e)
        except Exception as e:
            print(e.message)

    def getTrend(self, placeId, rank):
        try:
            Trend= TwitterTrend.objects.get(location= placeId, rank = rank)
        except TwitterTrend.DoesNotExist:
            Trend=None
        return Trend

class TweetApi:

    def tweet(self, include, reply, data):
        tweet=data.get("text", "")
        h = data.get('handler', None)
        wrap = TW_API.get(h, None)
        if include:
            inObj = Includable(include)
            tweet = tweet+" "+str(inObj)
        if reply:
            q=reply.get('topic', None)
            sr_list=SearchResult.objects.filter(query=q, autoPostStatus=None)[:1]
            print "length sr_list: "+str(sr_list)
            if len(sr_list)<1:
                search = Searching()
                search.search(data.get('handler'), reply.get('topic'))
            print "reply input: "+str(reply)
            r = Reply(reply)
            tweetId = r.getTweetId()
            screenName = r.getScreenName()
            tweet=wrap.replyTweet(tweet, screenName, tweetId)
            reply={"screenName": screenName, "tweetId": tweetId}

        else:
            wrap.postTweet(tweet)
        tw = Tweet()
        secret = TwitterSecret.objects.get(handler=h)
        tw.handler=secret
        tw.state="updated"
        tw.uuid= uuid.uuid4()
        tw.text=tweet
        tw.save()
        return Response({'tweet':tweet, "reply":reply})

class Searching(generics.ListAPIView):

    def get(self, request):
        print "calling get() in searching"
        wrap = TW_API.get('@tradStrat', None)
        query="atal pension"
        maxTweets=100
        try:
            listOfTweets= wrap.search(query, maxTweets)
            f = open(query+".txt",'w')
            for one in listOfTweets:
                f.write(str(one).encode('utf-8')+"\n")
        except Exception as e:
            print(str(e))

    def post(self, request):
        print "in post..."
        valid=['query', 'maxTweets', 'maxUsers', 'handler']
        mandatory=['query', 'handler']
        data = request.data
        input =data.keys()
        util.validate_mandatory_params(mandatory, input)
        util.validate_allowed_params(valid, input)
        q=data.get("query")
        m=data.get("maxTweets", 20)
        h=data.get("handler", None)
        if q is None:
            raise util.InvalidValue(msg="Invalid value given in 'query'")
        if h is None:
            raise util.InvalidValue(msg="Invalid value given in 'handler'")
        res = self.search(h, q, m)
        return Response(res)

    def saveResult(self, tweet, query):
        try:
            sr = SearchResult()
            sr.screenName = tweet.user.screen_name
            sr.tweetId = tweet.id
            sr.text = tweet.text
            sr.query=query
            #sr.tweetedTime = tweet.created_at
            sr.lang = tweet.lang
            sr.save()

        except Exception as e:
            if e[0] == 1366:
                print "Error no 1366, removing text"
                sr.text=None
                sr.save()
            else:
                raise e

    def search(self, handler, query, maxTweets=20):
        try:
            wrap = TW_API.get(handler, None)
            if wrap is None:
                raise util.NoSuchHandlerFound(handler=handler)
            listOfTweets = wrap.search(query, maxTweets)
            tweetCount = len(listOfTweets)
            newUsersCount=0
            for tweet in listOfTweets:
                try:
                    self.saveResult(tweet, query)
                    newUsersCount=newUsersCount+1
                except Exception as e:
                    print("an error: "+str(e))
        except util.TwitterError as e:
            print("an err occurred")
            raise e
        except util.TwitterRateLimitExceed:
            print("An err occurred, rate limit exceed")
            raise util.TwitterRateLimitExceed(handler=handler)
        return {"rowAdded": newUsersCount, "tweetCount": tweetCount}

class Reply:
    valid = ['topic', 'tweetNo']
    tweetId=None
    screenName=None

    def __init__(self,inputData):
        util.validate_allowed_params(self.valid, inputData.keys())
        topic=inputData.get('topic', None)
        print "in reply topic: "+str(topic)
        try:
            SRList = SearchResult.objects.filter(query=topic, autoPostStatus=None)[:1]
            print "length of sr list: "+str(len(SRList))
            if len(SRList)<1:
                raise util.NoSearchResultFound(topic=topic)
        except SearchResult.DoesNotExist:
            print "error..."
            raise util.NoSearchResultFound(msg='No search result found for query: '+str(topic))
        print("going ahead...")
        SR = SRList[0]
        self.tweetId = SR.tweetId
        self.screenName = SR.screenName
        SR.autoPostStatus = "used"
        SR.save()

    def getScreenName(self):
        return self.screenName

    def getTweetId(self):
        return self.tweetId

def twitter_startup():
    print "in tw startup"
    fill_tw_api()

