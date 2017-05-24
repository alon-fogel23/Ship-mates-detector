# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-24 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0025_soldier_sleep_time_pre_defined_max_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compartment_name', models.CharField(max_length=500)),
                ('compartment_classification', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='soldier',
            name='battle_stations_compartment',
            field=models.CharField(default='CIC', max_length=250),
        ),
    ]