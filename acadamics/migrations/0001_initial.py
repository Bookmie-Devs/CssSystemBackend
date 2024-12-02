# Generated by Django 5.1.3 on 2024-12-02 11:15

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(max_length=200)),
                ('level', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AcadamicSlides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='slides', verbose_name='Sildes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='acadamics.course')),
            ],
            options={
                'verbose_name_plural': 'Acadamic Slides',
            },
        ),
        migrations.CreateModel(
            name='OnlineTutorialTips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='resource_link')),
                ('type_of_resource', models.CharField(choices=[('slides', 'slides'), ('video', 'video'), ('audio', 'audio'), ('file', 'file')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='online_tips', to='acadamics.course')),
            ],
            options={
                'verbose_name_plural': 'Online Tutorial Tips',
            },
        ),
        migrations.CreateModel(
            name='PastQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='slides', verbose_name='Sildes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='past_questions', to='acadamics.course')),
            ],
            options={
                'verbose_name_plural': 'Past Questions',
            },
        ),
    ]
