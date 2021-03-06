# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    def forwards_func(apps, schema_editor):
        Record = apps.get_model("ship", "SingleRecord")
        Soldier = apps.get_model("ship", "Soldier")

        for r in Record.objects.all():
            r.soldier = Soldier.objects.get(tag=r.tag_string)
            r.save()

    dependencies = [
        ('ship', '0017_singlerecord_soldier_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlerecord',
            name='soldier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='records', to='ship.Soldier'),
        ),
        migrations.RunPython(forwards_func),
    ]
