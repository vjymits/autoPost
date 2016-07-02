# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0019_auto_20160618_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'18f5cef9-745f-4b32-b74e-afb28af605ec', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'2874f55a-65f0-4b1f-9f35-1847962c80a6', unique=True, editable=False),
        ),
    ]
