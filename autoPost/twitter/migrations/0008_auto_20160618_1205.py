# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0007_auto_20160618_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittersecret',
            name='updated',
            field=models.BigIntegerField(default=1466231702951L, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.CharField(default=b'c9a20b70-351e-11e6-b322-6451069f3666', max_length=64),
        ),
    ]
