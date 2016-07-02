__author__ = 'sharvija'
import twitter
from models import TwitterSecret, Tweet, TwitterTrend, Location
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import serializers
import util, const, json

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
        input =data.keys()
        allowed = ['text', 'img', 'handler', 'include']
        mandatory = ['handler']
        include = data.get('include', None)
        util.validate_mandatory_params(mandatory, input)
        util.validate_allowed_params(allowed, input)
        if include:
            inObj = Includable(include)
            textToInclude = inObj.__str__()

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
            util.validate_allowed_params(valid, trend.keys())
            placeId= trend.get('placeId', 1)
            rank= trend.get('rank', 1)
            tr = TwitterTrend.objects.get(location=placeId, rank=rank)
            tr_str=tr_str+' '+tr.name
        return tr_str

    def __str__(self):
        str = self.getTrends()+" "+self.users()
        return str


class TrendsApi:
    def fill_trends(self):
        all = Location.objects.all()
        for one in all:
            print "location: "+str(one.placeId)
            self.updateTrendsInDB(one.placeId)

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
            TwitterTrend.objects.all().delete()
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

def twitter_startup():
    print "in tw startup"
    fill_tw_api()

