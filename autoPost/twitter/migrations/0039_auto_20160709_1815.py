# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0038_auto_20160709_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'cecc3810-eb3c-4aeb-a9dd-0ac3ff668222', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'd73a15ed-8105-40cb-9a67-f3d03c021189', unique=True, editable=False),
        ),
    ]
