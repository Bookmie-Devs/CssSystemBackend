# Generated by Django 4.2.7 on 2025-01-07 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_remove_contactus_email_contactus_phone"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contactus",
            options={
                "verbose_name": "Reported Issue",
                "verbose_name_plural": "Reported Issues",
            },
        ),
    ]
