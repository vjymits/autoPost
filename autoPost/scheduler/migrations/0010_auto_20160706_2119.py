# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0009_auto_20160703_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduler',
            name='uuid',
            field=models.UUIDField(default=b'ed9e5ae4-3a10-48f4-886f-04955ad3aa4d', editable=False, unique=True, auto_created=True),
        ),
    ]
