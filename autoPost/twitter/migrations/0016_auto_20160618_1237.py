# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0015_twittersecret_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uuid', models.UUIDField(default=b'4eab03bc-5ebd-4670-89d5-84c56bd89a89', unique=True, editable=False)),
                ('text', models.CharField(max_length=256, null=True, blank=True)),
                ('img', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('state', models.CharField(default=b'new', max_length=10, choices=[(b'new', b'New'), (b'updated', b'Updated'), (b'failed', b'Failed'), (b'updating', b'Updating')])),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'ap_tweets',
            },
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'ef63fae6-baaf-466d-bd8f-9db8583741e3', unique=True, editable=False),
        ),
        migrations.AddField(
            model_name='tweet',
            name='secretId',
            field=models.ForeignKey(blank=True, to='twitter.TwitterSecret', null=True),
        ),
    ]
