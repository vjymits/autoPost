# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0014_remove_twittersecret_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'46e2b830-c128-4fc7-b329-b58420bf80fe', unique=True, editable=False),
        ),
    ]
