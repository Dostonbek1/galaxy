# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-25 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0118_influxsessionidentifier'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContentRule',
        ),
        migrations.AddField(
            model_name='importtaskmessage',
            name='score_type',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='importtaskmessage',
            name='content_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='importtaskmessage',
            name='linter_rule_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
