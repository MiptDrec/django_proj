# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20171217_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='age',
            field=models.CharField(max_length=8),
        ),
    ]
