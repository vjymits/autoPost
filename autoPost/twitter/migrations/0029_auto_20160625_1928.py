# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0028_auto_20160625_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('location', models.CharField(unique=True, max_length=100, db_column=b'location')),
                ('placeId', models.BigIntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='twittertrend',
            name='tweetVolume',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'2a5f80c8-1f05-4180-828c-2772d8998d36', editable=False, unique=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'4222cfa1-56bc-4d3a-8e84-c175f86f08cd', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittertrend',
            name='location',
            field=models.ForeignKey(db_column=b'location', to_field=b'location', to='twitter.Location', null=True),
        ),
        migrations.AlterField(
            model_name='twittertrend',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
