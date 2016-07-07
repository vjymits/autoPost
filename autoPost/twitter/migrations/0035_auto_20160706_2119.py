# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0034_auto_20160703_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoFollow',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uuid', models.UUIDField(unique=True, editable=False)),
                ('screenName', models.CharField(unique=True, max_length=15, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='searchresult',
            name='autoPostStatus',
            field=models.CharField(db_index=True, max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'b5b9a999-a664-426f-9a1e-0ff497e88e36', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'7ae1ac24-e3ba-435f-924a-5a672152d472', unique=True, editable=False),
        ),
        migrations.AddField(
            model_name='autofollow',
            name='handler',
            field=models.ForeignKey(db_column=b'handler', to_field=b'handler', blank=True, to='twitter.TwitterSecret', null=True),
        ),
    ]
