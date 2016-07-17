# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0041_auto_20160716_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='autofollow',
            name='query',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='autofollow',
            name='tweetId',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'c6139ecb-6cc2-438f-a953-427b3d910aa3', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'7429d752-55b7-4c28-b4be-956773f49d9c', unique=True, editable=False),
        ),
    ]
