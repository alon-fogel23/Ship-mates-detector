# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-01 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0036_auto_20170501_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewmode',
            name='view_mode',
            field=models.CharField(default='0', max_length=2),
        ),
    ]
