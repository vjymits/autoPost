# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0048_auto_20160718_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'9e331f4e-8d52-47ac-93bb-c8c99c9e231c', editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'7bc3c6fb-85cd-4edf-8c81-3cba66a161e1', editable=False, unique=True),
        ),
    ]
