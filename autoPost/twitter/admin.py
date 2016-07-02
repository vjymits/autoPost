from django.contrib import admin
from models import TwitterSecret, Location

class TwitterSecretAdmin(admin.ModelAdmin):
    fields = ['description', 'handler', 'app', 'consumerKey', 'consumerSecret', 'accessToken', 'accessTokenSecret']
    list_display = ['handler', 'description', 'app']

class TwitterLocationAdmin(admin.ModelAdmin):
    fields = ['location', 'placeId']
    list_display = fields

admin.site.register(TwitterSecret, TwitterSecretAdmin)
admin.site.register(Location, TwitterLocationAdmin)