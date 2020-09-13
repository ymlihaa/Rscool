# Generated by Django 3.0.8 on 2020-09-13 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_auto_20200913_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='content',
        ),
        migrations.CreateModel(
            name='LessonContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('content', models.FileField(upload_to='lesson-Content')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('lessonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.Lesson')),
            ],
        ),
    ]
