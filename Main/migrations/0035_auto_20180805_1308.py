# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-05 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0034_auto_20180805_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to='img/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]