# Generated by Django 4.2.7 on 2025-01-05 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_usersavedslides_usersavedpastqueations_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usersavedonlinetutorialtips",
            old_name="links",
            new_name="online_tips",
        ),
    ]
