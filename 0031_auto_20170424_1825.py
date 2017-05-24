# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-24 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0030_auto_20170424_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soldier',
            name='soldier_security_class',
        ),
        migrations.AlterField(
            model_name='compartment',
            name='compartment_security_class',
            field=models.IntegerField(default=1),
        ),
    ]
