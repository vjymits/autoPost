# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20160620_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduler',
            name='uuid',
            field=models.UUIDField(default=b'd7f390e0-a695-4227-b95a-3297c8574d22', editable=False, unique=True, auto_created=True),
        ),
    ]
