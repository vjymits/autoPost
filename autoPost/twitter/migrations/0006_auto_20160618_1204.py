# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_auto_20160618_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittersecret',
            name='updated',
            field=models.BigIntegerField(default=1466231644825L, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.CharField(default=b'a6fc9180-351e-11e6-b2d4-6451069f3666', max_length=64),
        ),
    ]
