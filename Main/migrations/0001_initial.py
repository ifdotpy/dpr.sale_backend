# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-27 18:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Города',
                'verbose_name': 'Город',
            },
        ),
        migrations.CreateModel(
            name='CustomData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(verbose_name='Статус')),
                ('phone', models.CharField(blank=True, max_length=25, null=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Fastoran',
                'verbose_name': 'Fastoran',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Название')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.City', verbose_name='Город')),
            ],
            options={
                'verbose_name_plural': 'Районы',
                'verbose_name': 'Район',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to='filer.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_top', models.BooleanField(verbose_name='В топе')),
                ('main_photo', models.ImageField(upload_to='title_photos', verbose_name='Главное изображение')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Стоимость')),
                ('currency', models.IntegerField(choices=[(0, 'Рубль'), (1, 'Доллар')], verbose_name='Валюта')),
                ('verified', models.BooleanField(default=False, verbose_name='Подтвержден')),
                ('closed', models.BooleanField(default=False, verbose_name='Закрыт')),
                ('reason', models.TextField(blank=True, null=True, verbose_name='Причина')),
                ('rooms', models.PositiveSmallIntegerField(default=1, verbose_name='Количество комнат')),
                ('floor', models.PositiveSmallIntegerField(default=1, verbose_name='Этаж')),
                ('square', models.FloatField(default=1, verbose_name='Площадь (метры кв.)')),
                ('storeys', models.PositiveSmallIntegerField(default=1, verbose_name='Этажность здания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Category', verbose_name='Категория')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.District', verbose_name='Район')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Post'),
        ),
    ]