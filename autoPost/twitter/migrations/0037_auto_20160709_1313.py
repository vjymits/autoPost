# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0036_auto_20160707_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'035f57aa-a89c-44de-bf31-035617c0f8ab', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'9aede457-befe-4659-b515-42fb8eb5570a', unique=True, editable=False),
        ),
    ]
