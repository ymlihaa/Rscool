# Generated by Django 3.0.8 on 2020-09-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0006_auto_20200913_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi'),
        ),
    ]
