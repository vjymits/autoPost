# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0012_auto_20160709_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='restscheduler',
            name='every',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='restscheduler',
            name='maxRuns',
            field=models.IntegerField(default=0),
        ),
    ]
