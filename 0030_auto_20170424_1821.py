# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-24 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0029_remove_compartment_compartment_sensor_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compartment',
            name='compartment_classification',
        ),
        migrations.AddField(
            model_name='compartment',
            name='compartment_security_class',
            field=models.CharField(default='BALMAS', max_length=250),
        ),
        migrations.AddField(
            model_name='soldier',
            name='soldier_security_class',
            field=models.CharField(default='BALMAS', max_length=250),
        ),
    ]
