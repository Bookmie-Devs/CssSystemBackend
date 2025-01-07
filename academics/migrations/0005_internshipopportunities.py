# Generated by Django 4.2.7 on 2025-01-07 13:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("academics", "0004_alter_academicslides_title_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="InternshipOpportunities",
            fields=[
                (
                    "internship_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("campany_name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("registration_link", models.URLField()),
                ("application_deadline", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]