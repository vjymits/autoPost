# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0032_auto_20160625_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('uuid', models.UUIDField(default=b'134d6e2f-1d05-441f-8b25-e196a99c4896', editable=False, unique=True, auto_created=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('query', models.CharField(max_length=40, db_index=True)),
                ('screenName', models.CharField(unique=True, max_length=15, db_index=True)),
                ('tweetId', models.BigIntegerField(unique=True)),
                ('text', models.CharField(max_length=200, null=True, blank=True)),
                ('lang', models.CharField(default=b'en', max_length=10)),
                ('extra', models.CharField(max_length=500, null=True, blank=True)),
                ('autoPostStatus', models.CharField(max_length=15, null=True, blank=True)),
                ('tweetedTime', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'006e8e91-9673-460e-be15-f955fd69b30b', editable=False, unique=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='handler',
            field=models.CharField(unique=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'08ed4e86-2f5c-4c62-bc39-a550082de1ae', unique=True, editable=False),
        ),
    ]
