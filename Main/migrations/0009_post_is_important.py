# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-28 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_auto_20171006_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_important',
            field=models.BooleanField(default=False, verbose_name='Срочно'),
        ),
    ]
