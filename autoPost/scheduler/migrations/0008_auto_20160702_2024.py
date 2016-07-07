# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_auto_20160625_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduler',
            name='uuid',
            field=models.UUIDField(default=b'e47a9a12-6006-4102-b083-1c61ca6d82dd', editable=False, unique=True, auto_created=True),
        ),
    ]
