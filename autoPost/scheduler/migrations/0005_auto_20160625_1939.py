# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20160625_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduler',
            name='uuid',
            field=models.UUIDField(default=b'b78c2f29-f64c-4250-8aab-c3d29c2b1dfc', editable=False, unique=True, auto_created=True),
        ),
    ]
