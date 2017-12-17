# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='type',
        ),
        migrations.AddField(
            model_name='activities',
            name='category',
            field=models.CharField(max_length=3, default='non', choices=[('lep', 'Лепка'), ('mat', 'Математика')]),
        ),
        migrations.AlterField(
            model_name='activities',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
