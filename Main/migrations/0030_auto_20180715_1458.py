# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-15 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0029_auto_20180715_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='archive',
            new_name='is_archive',
        ),
    ]