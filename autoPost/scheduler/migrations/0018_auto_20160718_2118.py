# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 15:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0017_auto_20160718_2033'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='actionscheduler',
            table='ap_act_scheduler',
        ),
    ]