# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0012_auto_20160618_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(unique=True),
        ),
    ]
