# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_sets_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sets',
            name='pic',
            field=models.ImageField(upload_to='photos', verbose_name='Photo'),
        ),
    ]
