# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0031_auto_20160625_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'3c2b71d5-915b-4949-a4e7-1eec38280fa8', editable=False, unique=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'5f5eba17-9f60-4568-8bf9-c522fec9fc5d', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittertrend',
            name='location',
            field=models.BigIntegerField(default=0),
        ),
    ]
