# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-24 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0022_auto_20170424_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singlerecord',
            name='delta_time',
        ),
    ]
