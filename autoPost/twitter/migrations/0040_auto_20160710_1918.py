# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0039_auto_20160709_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoFollowPolicy',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uuid', models.UUIDField(unique=True, editable=False)),
                ('retainFollowers', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='autofollow',
            name='status',
            field=models.CharField(default=b'new', max_length=20, db_index=True),
        ),
        migrations.AddField(
            model_name='autofollow',
            name='userId',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='searchresult',
            name='userId',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='autofollow',
            name='screenName',
            field=models.CharField(max_length=15, db_index=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'10d06cdf-d80b-493c-99b9-c9f5bbb998cd', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'7b9f7f5c-47bf-4d10-8740-e07dd3426f9f', unique=True, editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='autofollow',
            unique_together=set([('userId', 'handler')]),
        ),
        migrations.AddField(
            model_name='autofollowpolicy',
            name='handler',
            field=models.ForeignKey(db_column=b'handler', to_field=b'handler', blank=True, to='twitter.TwitterSecret', null=True),
        ),
    ]
