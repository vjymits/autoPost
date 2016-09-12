from django.db import models
from util import TWEET_STATES, get_current_time_integer
import uuid

class TwitterSecret(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(max_length=64, unique=True, default=str(uuid.uuid4()), editable=False)
    description = models.CharField(max_length=256, blank=True, null=True)
    handler = models.CharField(max_length=16, unique=True)
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
    uuid = models.UUIDField(max_length=64, unique=True, default=str(uuid.uuid4()), editable=False,)
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

class SearchResult(models.Model):
    id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=256, db_index=True)
    screenName = models.CharField(max_length=15, db_index=True, unique=True)
    userId = models.BigIntegerField(null=True, blank=True)
    tweetId = models.BigIntegerField(unique=True)
    text = models.CharField(max_length=200, blank=True, null=True)
    lang = models.CharField(max_length=10, default='en')
    extra = models.CharField(max_length=500, null=True, blank=True)
    autoPostStatus = models.CharField(max_length=15, null=True, blank=True, db_index=True)
    tweetedTime = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "screenName: "+str(self.screenName)+" text: "+str(self.text)


class AutoFollowPolicy(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(max_length=32, unique=True, editable=False,)
    handler = models.ForeignKey(TwitterSecret, to_field='handler', db_column='handler', blank=True, null=True)
    retainFollowers=models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

class AutoFollow(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(max_length=32, unique=True, editable=False,)
    screenName = models.CharField(max_length=15, db_index=True)
    userId=models.BigIntegerField(null=True, blank=True)
    handler = models.ForeignKey(TwitterSecret, to_field='handler', db_column='handler', blank=True, null=True)
    tweetId = models.BigIntegerField(default=0)
    query = models.CharField(max_length=256, null=True, blank=True)
    status=models.CharField(max_length=20, default='new', db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    expireInDays = models.IntegerField(default=30)

    class Meta:
        unique_together=('userId', 'handler')

    def __str__(self):
        return "screen: "+str(self.screenName)+" handler: "+str(self.handler)+" status: "+str(self.status)

class DirectMsg(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(max_length=32, unique=True, editable=False,)
    screenName = models.CharField(max_length=15, db_index=True)
    userId=models.BigIntegerField(null=True, blank=True)
    handler = models.ForeignKey(TwitterSecret, to_field='handler', db_column='handler', blank=True, null=True)
    msg=models.models.CharField(max_length=500, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ap_twitter_dm'
