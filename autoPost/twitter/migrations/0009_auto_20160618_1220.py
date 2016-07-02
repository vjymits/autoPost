# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0008_auto_20160618_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittersecret',
            name='updated',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.CharField(default=b'edfb6500-3520-11e6-9ba3-6451069f3666', max_length=64),
        ),
    ]
