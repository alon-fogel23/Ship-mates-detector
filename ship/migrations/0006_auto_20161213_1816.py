# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0005_auto_20161213_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlerecord',
            name='tag_string',
            field=models.CharField(default='0x00 0x00 0x00 0x00', max_length=250),
        ),
    ]