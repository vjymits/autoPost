# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0013_auto_20160709_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restscheduler',
            name='frequency',
            field=models.CharField(default=b'hourly', max_length=20, choices=[(b'hourly', b'Hourly'), (b'weekly', b'Weekly'), (b'minutly', b'Minutly'), (b'daily', b'Daily'), (b'yearly', b'Yearly')]),
        ),
        migrations.AlterField(
            model_name='restscheduler',
            name='schedulerType',
            field=models.CharField(default=b'Interval', max_length=10, choices=[(b'interval', b'Interval'), (b'cron', b'Cron')]),
        ),
    ]
