# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-05 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import os


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Image = apps.get_model("Main", "Image")
    FilerFileField = apps.get_model("filer", "File")
    db_alias = schema_editor.connection.alias
    qs = Image.objects.using(db_alias).all()
    for obj in qs:
        try:
            print(obj.image_file.url)
            file = FilerFileField.objects.using(db_alias).get(id=os.path.basename(obj.image_file.path),)
            print(f'From {obj.image_file.path} to {"img/"+str(file.file)}')
            obj.image_file = 'img/' + str(file.file)

            obj.save()
        except:
            print(f'Leave {obj.image_file.url}')
            pass






def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0037_auto_20180805_2055'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]