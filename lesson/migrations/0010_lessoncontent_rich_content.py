# Generated by Django 3.0.8 on 2020-09-13 21:16

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0009_lesson_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessoncontent',
            name='rich_content',
            field=djrichtextfield.models.RichTextField(blank=True, null=True),
        ),
    ]
