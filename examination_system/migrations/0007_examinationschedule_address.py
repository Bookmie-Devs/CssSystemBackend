# Generated by Django 5.1.3 on 2024-12-20 14:23

import django_google_maps.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("examination_system", "0006_remove_examinationschedule_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="examinationschedule",
            name="address",
            field=django_google_maps.fields.AddressField(default="", max_length=200),
            preserve_default=False,
        ),
    ]
