# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterSecrets',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uuid', models.CharField(default=b'2e5b5930-3516-11e6-9cbc-6451069f3666', max_length=64)),
                ('description', models.CharField(max_length=256, null=True, blank=True)),
                ('handler', models.CharField(unique=True, max_length=100)),
                ('app', models.CharField(unique=True, max_length=100)),
                ('consumerKey', models.CharField(unique=True, max_length=100)),
                ('consumerSecret', models.CharField(unique=True, max_length=100)),
                ('accessToken', models.CharField(unique=True, max_length=100)),
                ('accessTokenSecret', models.CharField(unique=True, max_length=100)),
            ],
        ),
    ]
