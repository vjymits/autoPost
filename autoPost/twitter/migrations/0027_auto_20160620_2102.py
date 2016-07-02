# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0026_auto_20160619_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='secret',
        ),
        migrations.AddField(
            model_name='tweet',
            name='handler',
            field=models.ForeignKey(db_column=b'handler', to_field=b'handler', blank=True, to='twitter.TwitterSecret', null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'e020d06f-1555-42e0-9891-7a639e99405d', editable=False, unique=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'955c50c5-e701-4d10-b931-13fe919feece', unique=True, editable=False),
        ),
    ]
