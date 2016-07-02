from django.db import models
from scheduler.util import FREQUENCIES, SCHDULER_TYPE
import uuid

class Scheduler(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(max_length=64, unique=True, default=str(uuid.uuid4()), editable=False,
                            auto_created=True)
    name= models.CharField(max_length=100, unique=True)
    frequency = models.CharField(max_length=20, choices=FREQUENCIES, default=FREQUENCIES[0][0])
    schedulerType = models.CharField(max_length=10, choices=SCHDULER_TYPE, default=SCHDULER_TYPE[0][0])
    function = models.Func(max_length=32, null=True, blank=True)
    exprn = models.CharField(max_length=32, null=True, blank=True)
    args = models.CharField(max_length=1024, null=True, blank=True)
    kwargs = models.CharField(max_length=1024, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table= "ap_scheduler"