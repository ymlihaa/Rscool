# Generated by Django 3.0.8 on 2020-09-13 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0007_auto_20200913_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessoncontent',
            name='content',
            field=models.FileField(blank=True, upload_to='lesson-Content'),
        ),
    ]
