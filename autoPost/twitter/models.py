from django.db import models
from util import TWEET_STATES, get_current_time_integer
import uuid

class TwitterSecret(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(max_length=64, unique=True, default=str(uuid.uuid4()), editable=False)
    description = models.CharField(max_length=256, blank=True, null=True)
    handler = models.CharField(max_length=100, unique=True)
    app = models.CharField(max_length=100, unique=True)
    consumerKey = models.CharField(max_length=100, unique=True)
    consumerSecret = models.CharField(max_length=100, unique=True)
    accessToken = models.CharField(max_length=100, unique=True)
    accessTokenSecret = models.CharField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ap_twitter_secrets'

class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(max_length=64, unique=True, default=str(uuid.uuid4()), editable=False,
                            auto_created=True)
    text = models.CharField(max_length=140, blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    handler = models.ForeignKey(TwitterSecret, to_field= 'handler', db_column= 'handler', blank=True, \
                                                                                         null=True)
    state = models.CharField(max_length=10, choices=TWEET_STATES, default=TWEET_STATES[0][0])
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ap_tweets'

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100, unique=True, db_column='location')
    placeId = models.BigIntegerField(unique=True)

class TwitterTrend(models.Model):
    id = models.AutoField(primary_key=True)
    rank = models.IntegerField(default=0)
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.BigIntegerField(default=0)
    tweetVolume= models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ap_twitter_trends'



