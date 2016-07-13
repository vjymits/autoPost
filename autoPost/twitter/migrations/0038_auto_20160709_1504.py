# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0037_auto_20160709_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'dcc628df-410a-4636-b300-174918b5b366', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'102b1d94-c3e5-4d17-a1ad-8642b9e6219e', unique=True, editable=False),
        ),
    ]
