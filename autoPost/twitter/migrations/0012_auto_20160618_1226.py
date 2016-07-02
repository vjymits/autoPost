# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0011_auto_20160618_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittersecret',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 18, 6, 56, 36, 211000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
