# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-18 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confession_wall', '0008_auto_20180315_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confession',
            name='motion',
            field=models.CharField(choices=[('To', 'To'), ('Find', 'Find')], default='To', max_length=5),
        ),
        migrations.AlterField(
            model_name='confession',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
