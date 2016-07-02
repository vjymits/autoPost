# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0006_auto_20160618_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittersecret',
            name='updated',
            field=models.BigIntegerField(default=1466231692978L, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.CharField(default=b'c3b0491e-351e-11e6-87ea-6451069f3666', max_length=64),
        ),
    ]
