# Generated by Django 5.1.3 on 2024-12-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_news_views"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="views",
            field=models.IntegerField(default=0),
        ),
    ]
