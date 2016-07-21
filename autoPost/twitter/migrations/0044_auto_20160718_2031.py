# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0043_auto_20160716_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchresult',
            name='query',
            field=models.CharField(db_index=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'f0bbbc57-82fc-40fc-9862-27745637b695', editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'5186d8e2-bdf9-4269-9d0b-d610db24505c', editable=False, unique=True),
        ),
    ]
