# Generated by Django 4.2.7 on 2025-01-05 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_alter_news_back_image_alter_news_head_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={"verbose_name": "News/Blogs", "verbose_name_plural": "News/Blogs"},
        ),
        migrations.AlterModelTable(
            name="news",
            table="news_blogs",
        ),
    ]
