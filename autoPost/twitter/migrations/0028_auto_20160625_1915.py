# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0027_auto_20160620_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twittertrend',
            old_name='text',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(max_length=140, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'99e570b4-311b-4d53-8020-87d8e8f4e89f', editable=False, unique=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'd558ae47-ab58-4fc2-81cd-246f4200cf41', unique=True, editable=False),
        ),
    ]
