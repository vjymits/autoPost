# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('uuid', models.UUIDField(default=b'2a45aa1b-641a-4262-a094-ebff851c20f7', editable=False, unique=True, auto_created=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('frequency', models.CharField(default=b'Hourly', max_length=20, choices=[(b'Hourly', b'hourly'), (b'Weekly', b'weekly'), (b'Minutly', b'minutly'), (b'Daily', b'daily'), (b'Yearly', b'yearly')])),
                ('schedulerType', models.CharField(default=b'interval', max_length=10, choices=[(b'interval', b'Interval'), (b'cron', b'Cron')])),
                ('exprn', models.CharField(max_length=32, null=True, blank=True)),
                ('args', models.CharField(max_length=1024, null=True, blank=True)),
                ('kwargs', models.CharField(max_length=1024, null=True, blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'ap_scheduler',
            },
        ),
    ]
