"""autoPost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from twitter.views import search, post_tweet, update_trend, auto_follow, test, un_follow
from twitter.api import TweetList, twitter_startup
from scheduler.api import sch_startup

BASE_URI_V1 = r'^rest/smm/v1/'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(BASE_URI_V1+'tweet/$', post_tweet),
    url(BASE_URI_V1+'search/$', search),
    url(BASE_URI_V1+'trends/$', update_trend),
    url(BASE_URI_V1+'autoFollow/$', auto_follow),
    url(BASE_URI_V1+'unFollow/$', un_follow),
    url(BASE_URI_V1+'test/$', test)
]

def startup():
    twitter_startup()
    sch_startup()

startup()