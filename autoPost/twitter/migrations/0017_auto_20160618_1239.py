# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0016_auto_20160618_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='secretId',
            new_name='secret',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'ba2b1e38-0f35-479e-bb27-500407149304', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'3ca338f2-66ba-4b09-9899-de4e0896fb6f', unique=True, editable=False),
        ),
    ]
