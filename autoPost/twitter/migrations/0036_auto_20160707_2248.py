# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0035_auto_20160706_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'4951e5a3-a906-4ef1-ac53-7c2bf91adf3d', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'69cefa2d-1881-458c-be43-397bf1faddac', unique=True, editable=False),
        ),
    ]
