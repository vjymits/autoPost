from django.contrib import admin
from models import RestScheduler

class RestSchedulerAdmin(admin.ModelAdmin):
    fields = ['name', 'frequency', 'every', 'method', 'URI', 'requestBody', 'schedulerType', 'exprn']
    list_display = ['name', 'frequency', 'method', 'URI']

admin.site.register(RestScheduler, RestSchedulerAdmin)