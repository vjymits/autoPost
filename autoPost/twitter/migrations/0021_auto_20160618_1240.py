# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0020_auto_20160618_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='uuid',
            field=models.UUIDField(default=b'26cd8472-3f9f-4ee1-9e91-8a2a1ef3bda4', editable=False, unique=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='twittersecret',
            name='uuid',
            field=models.UUIDField(default=b'9f1427ea-7588-41ac-a0a7-cb1df5abee55', unique=True, editable=False),
        ),
    ]
