# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-15 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0031_auto_20180715_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_closed',
            new_name='closed',
        ),
    ]