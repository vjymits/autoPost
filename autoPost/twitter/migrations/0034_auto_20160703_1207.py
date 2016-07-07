# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0033_auto_20160702_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchresult',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'bc179278-3173-4ffa-afee-632fcbfea26b', editable=False, unique=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'32e17367-8bf6-4e84-8c5d-78a83060a096', unique=True, editable=False),
        ),
    ]
