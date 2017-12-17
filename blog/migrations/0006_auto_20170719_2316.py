# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='category',
            field=models.CharField(max_length=3, default='non', choices=[('lep', 'Лепка'), ('mat', 'Математика'), ('dra', 'Рисование'), ('mot', 'Моторика')]),
        ),
    ]
