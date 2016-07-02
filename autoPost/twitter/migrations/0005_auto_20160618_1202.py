# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_auto_20160618_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittersecret',
            name='updated',
            field=models.BigIntegerField(default=1466231530250L, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.CharField(default=b'62b1cf91-351e-11e6-93f0-6451069f3666', max_length=64),
        ),
    ]
