# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-15 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confession_wall', '0006_auto_20180315_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='location_from',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='location_to',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
