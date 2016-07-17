# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0042_auto_20160716_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autofollow',
            name='expireInDays',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'7020e43c-5a99-45b5-ab54-f0817c66131d', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'e26d62fc-d7ba-47ee-a95f-8edd0761104c', unique=True, editable=False),
        ),
    ]
