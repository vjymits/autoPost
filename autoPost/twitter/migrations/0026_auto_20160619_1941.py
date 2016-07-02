# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0025_auto_20160619_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'd5478fc1-9dc0-4c27-8fbf-402b5f3d83c1', editable=False, unique=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'9be73706-488e-4183-9d2f-09f142cb28e2', unique=True, editable=False),
        ),
    ]
