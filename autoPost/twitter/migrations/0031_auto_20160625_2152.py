# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0030_auto_20160625_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='twittertrend',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'642b2102-d775-4a85-a945-6a4bd6f35030', editable=False, unique=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'266d044a-d1b9-4740-bc8a-a8041d4b398b', unique=True, editable=False),
        ),
    ]
