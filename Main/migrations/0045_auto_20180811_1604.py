# Generated by Django 2.0.8 on 2018-08-11 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0044_auto_20180811_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district', to='Main.City', verbose_name='Город'),
        ),
    ]
