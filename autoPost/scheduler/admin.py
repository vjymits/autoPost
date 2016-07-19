from django.contrib import admin
from models import RestScheduler, ActionScheduler

class RestSchedulerAdmin(admin.ModelAdmin):
    fields = ['name', 'frequency', 'every', 'method', 'URI', 'requestBody', 'schedulerType', 'exprn']
    list_display = ['name', 'frequency', 'method', 'URI']

class ActSchedulerAdmin(admin.ModelAdmin):
    fields = ['name', 'frequency', 'every','action', 'requestBody', 'schedulerType', 'exprn']
    list_display = ['name', 'frequency', 'action']

admin.site.register(RestScheduler, RestSchedulerAdmin)
admin.site.register(ActionScheduler, ActSchedulerAdmin)

