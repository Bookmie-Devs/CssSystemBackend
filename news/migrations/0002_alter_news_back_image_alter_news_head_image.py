# Generated by Django 4.2.7 on 2024-12-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="back_image",
            field=models.ImageField(null=True, upload_to="news"),
        ),
        migrations.AlterField(
            model_name="news",
            name="head_image",
            field=models.ImageField(null=True, upload_to="news"),
        ),
    ]
