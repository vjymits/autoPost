# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0009_auto_20160618_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.CharField(default=b'f471e7ae-3520-11e6-8651-6451069f3666', max_length=64),
        ),
    ]
