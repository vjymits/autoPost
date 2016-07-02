# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0022_auto_20160618_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterTrend',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=256, null=True, blank=True)),
                ('location', models.BigIntegerField(max_length=32, null=True, blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'ap_twitter_trends',
            },
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'0b3715e4-7636-4b9c-b6d8-cd7d7becd5ba', editable=False, unique=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'ea6ef25c-c9a6-48b7-a0ea-61cacff84cf9', unique=True, editable=False),
        ),
    ]
