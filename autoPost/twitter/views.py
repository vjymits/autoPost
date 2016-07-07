from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import Searching, TweetList, TrendsApi

@api_view(['POST'])
def search(req):
    search=Searching()
    return search.post(req)

@api_view(['POST'])
def post_tweet(req):
    t=TweetList()
    return t.post(req)

@api_view(['PUT', 'GET'])
def update_trend(req):
    TrendsApi().fill_trends()




