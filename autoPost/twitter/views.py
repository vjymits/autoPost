from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import Searching, TweetList, TrendsApi, AutoFollowApi
from models import SearchResult, AutoFollow

@api_view(['POST'])
def search(req):
    search=Searching()
    return search.post(req.data)

@api_view(['POST'])
def post_tweet(req):
    t=TweetList()
    return t.post(req.data)

@api_view(['PUT', 'GET'])
def update_trend(req):
    return TrendsApi().fill_trends()

@api_view(['POST','PUT'])
def auto_follow(req):
    return AutoFollowApi().follow(req.data)

@api_view(['POST', 'PUT'])
def un_follow(req):
    return AutoFollowApi().unFollow(req.data)

@api_view(['POST','PUT', 'GET', 'DELETE'])
def test(req):
    print "in test()"
    s = SearchResult.objects.filter(query='#shair').exclude(id__in= AutoFollow.objects.filter(
            handler='@vjymits', status = 'new'))[:1]
    print str(s)
    return Response("OK")
