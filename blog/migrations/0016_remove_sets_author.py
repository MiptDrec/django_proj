# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 13:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_sets_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sets',
            name='author',
        ),
    ]
