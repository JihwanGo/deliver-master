# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0003_auto_20171120_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='institution',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
