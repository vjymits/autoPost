# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20160618_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='twittersecret',
            name='updated',
            field=models.BigIntegerField(default=1466231424596L, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.CharField(default=b'23b84a30-351e-11e6-9acc-6451069f3666', max_length=64),
        ),
    ]
