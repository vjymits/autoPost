# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0013_auto_20160618_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twittersecret',
            name='uuid',
        ),
    ]
