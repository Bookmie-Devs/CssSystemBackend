# Generated by Django 5.1.4 on 2025-01-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academics", "0005_internshipopportunities"),
    ]

    operations = [
        migrations.AddField(
            model_name="internshipopportunities",
            name="image",
            field=models.ImageField(null=True, upload_to="internships"),
        ),
    ]