# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0047_auto_20160718_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'72013da8-2816-4cd8-80ca-21c61f531546', editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'9e9be113-3de0-4979-93ca-f8cc72be733b', editable=False, unique=True),
        ),
    ]
