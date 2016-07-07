# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0008_auto_20160702_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduler',
            name='uuid',
            field=models.UUIDField(default=b'cb107d7f-6c6d-442d-9814-0af43abbdc0e', editable=False, unique=True, auto_created=True),
        ),
    ]
