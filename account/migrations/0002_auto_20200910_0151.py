# Generated by Django 3.0.8 on 2020-09-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=255, unique=True, verbose_name='username'),
        ),
    ]
