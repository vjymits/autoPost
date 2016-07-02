# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0010_auto_20160618_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(),
        ),
    ]
