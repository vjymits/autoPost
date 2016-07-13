# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_auto_20160706_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestScheduler',
            fields=[
                ('uuid', models.UUIDField(default=b'6cfff43b-1bdc-4575-a92c-607afbb6021a', editable=False, unique=True, auto_created=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('frequency', models.CharField(default=b'Hourly', max_length=20, choices=[(b'Hourly', b'hourly'), (b'Weekly', b'weekly'), (b'Minutly', b'minutly'), (b'Daily', b'daily'), (b'Yearly', b'yearly')])),
                ('schedulerType', models.CharField(default=b'interval', max_length=10, choices=[(b'interval', b'Interval'), (b'cron', b'Cron')])),
                ('method', models.CharField(default=b'GET', max_length=10, choices=[(b'GET', b'GET'), (b'POST', b'POST'), (b'PUT', b'PUT'), (b'DELETE', b'DELETE'), (b'HEAD', b'HEAD')])),
                ('URI', models.URLField(max_length=256, null=True, blank=True)),
                ('requestBody', models.TextField(max_length=2048, null=True)),
                ('exprn', models.CharField(max_length=32, null=True, blank=True)),
                ('args', models.CharField(max_length=1024, null=True, blank=True)),
                ('kwargs', models.CharField(max_length=1024, null=True, blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'ap_rest_scheduler',
            },
        ),
        migrations.DeleteModel(
            name='Scheduler',
        ),
    ]
