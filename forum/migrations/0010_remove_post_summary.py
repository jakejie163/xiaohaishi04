# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-17 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20180224_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='summary',
        ),
    ]
