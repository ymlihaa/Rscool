# Generated by Django 3.0.8 on 2020-09-13 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lesson', '0008_auto_20200913_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='userID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
