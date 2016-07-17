# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0040_auto_20160710_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='autofollow',
            name='expireInDays',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='autofollow',
            name='tweetId',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'2a401d48-79f7-42e2-9ed3-3049378a6e66', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'1538c4be-5a6f-42fa-ae32-8c1013ff2a67', unique=True, editable=False),
        ),
    ]
