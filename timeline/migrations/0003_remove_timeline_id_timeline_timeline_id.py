# Generated by Django 5.1.3 on 2024-12-02 11:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_timeline_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeline',
            name='id',
        ),
        migrations.AddField(
            model_name='timeline',
            name='timeline_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]