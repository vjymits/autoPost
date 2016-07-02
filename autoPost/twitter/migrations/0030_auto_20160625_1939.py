# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0029_auto_20160625_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'09b49a50-841e-4f0c-9ef6-188c5cf8a4a1', editable=False, unique=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'8b8e6816-6a75-4046-93b1-59aa0b4c38fc', unique=True, editable=False),
        ),
    ]
