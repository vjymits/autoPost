# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0050_auto_20160719_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'2b984007-a060-46c1-88f3-04ba6f48f4c9', editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'cba6294e-dd06-481d-85bf-1a30e6fbf56f', editable=False, unique=True),
        ),
    ]
