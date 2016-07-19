from django.db import models
from scheduler.util import FREQUENCIES, SCHDULER_TYPE, REST_METHODS, SCH_ACTIONS
from scheduler.api import SchedulerApi
import uuid

api = SchedulerApi()

class RestScheduler(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(max_length=64, unique=True, auto_created=True, editable=False)
    name= models.CharField(max_length=100, unique=True)
    frequency = models.CharField(max_length=20, choices=FREQUENCIES, default=FREQUENCIES[0][0])
    every = models.IntegerField(default=1)
    maxRuns = models.IntegerField(default=0)
    schedulerType = models.CharField(max_length=10, choices=SCHDULER_TYPE, default=SCHDULER_TYPE[0][1])
    function = models.Func(max_length=32, null=True, blank=True)
    method = models.CharField(max_length=10, choices=REST_METHODS, default=REST_METHODS[0][0])
    URI = models.CharField(max_length=256, null=True, blank=True)
    requestBody = models.TextField(max_length=2048, null=True, blank=True)
    exprn = models.CharField(max_length=32, null=True, blank=True)
    args = models.CharField(max_length=1024, null=True, blank=True)
    kwargs = models.CharField(max_length=1024, null=True, blank=True)
    lastRunTime=models.DateTimeField(null=True, blank=True)
    nextRunTime=models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table= "ap_rest_scheduler"

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        self.nextRunTime = api.createScheduler(self.toDict()).get('nextRunTime', None)
        super(RestScheduler, self).save(*args, **kwargs)

    def toDict(self):
        data={}
        data['uuid'] = self.uuid
        data['name'] = self.name
        data['frequency'] = self.frequency
        data['schedulerType'] = self.schedulerType
        data['method'] = self.method
        data['every'] = self.every
        data['uri'] = self.URI
        data['requestBody'] = self.requestBody
        data['exprn'] = self.exprn
        return data

    def delete(self, using=None):
        uuid = self.uuid
        api.deleteScheduler(str(uuid))
        super(RestScheduler, self).delete(using)


class ActionScheduler(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(max_length=64, unique=True, auto_created=True, editable=False)
    name= models.CharField(max_length=100, unique=True)
    frequency = models.CharField(max_length=20, choices=FREQUENCIES, default=FREQUENCIES[0][0])
    every = models.IntegerField(default=1)
    maxRuns = models.IntegerField(default=0)
    schedulerType = models.CharField(max_length=10, choices=SCHDULER_TYPE, default=SCHDULER_TYPE[0][1])
    action = models.CharField(max_length=32, choices=SCH_ACTIONS, default=SCH_ACTIONS[0][0])
    requestBody = models.TextField(max_length=2048, null=True, blank=True)
    exprn = models.CharField(max_length=32, null=True, blank=True)
    args = models.CharField(max_length=1024, null=True, blank=True)
    kwargs = models.CharField(max_length=1024, null=True, blank=True)
    lastRunTime=models.DateTimeField(null=True, blank=True)
    nextRunTime=models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table= "ap_act_scheduler"

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        self.nextRunTime = api.createActScheduler(self.toDict()).get('nextRunTime', None)
        super(ActionScheduler, self).save(*args, **kwargs)

    def toDict(self):
        data={}
        data['uuid'] = self.uuid
        data['name'] = self.name
        data['frequency'] = self.frequency
        data['schedulerType'] = self.schedulerType
        data['every'] = self.every
        data['action'] = self.action
        data['requestBody'] = self.requestBody
        data['exprn'] = self.exprn
        return data

    def delete(self, using=None):
        uuid = self.uuid
        api.deleteScheduler(str(uuid))
        super(ActionScheduler, self).delete(using)