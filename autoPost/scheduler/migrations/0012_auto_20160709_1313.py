# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0011_auto_20160707_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='restscheduler',
            name='lastRunTime',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='restscheduler',
            name='nextRunTime',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restscheduler',
            name='URI',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restscheduler',
            name='requestBody',
            field=models.TextField(max_length=2048, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restscheduler',
            name='uuid',
            field=models.UUIDField(editable=False, unique=True, auto_created=True),
        ),
    ]
