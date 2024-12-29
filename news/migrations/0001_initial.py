# Generated by Django 4.2.7 on 2024-12-29 15:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "news_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("reported_by", models.CharField(max_length=100)),
                ("report", models.TextField()),
                ("minutes_read", models.IntegerField(default=0)),
                (
                    "head_image",
                    models.ImageField(blank=True, null=True, upload_to="news"),
                ),
                (
                    "back_image",
                    models.ImageField(blank=True, null=True, upload_to="news"),
                ),
                ("views", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updted", models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                "verbose_name_plural": "News",
            },
        ),
    ]
