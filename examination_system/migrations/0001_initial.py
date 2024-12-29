# Generated by Django 4.2.7 on 2024-12-29 15:44

from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("academics", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExaminationSchedule",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("index_number_start", models.CharField(default=0, max_length=230)),
                ("index_number_end", models.CharField(default=0, max_length=230)),
                ("time", models.DateTimeField(null=True)),
                ("college", models.CharField(max_length=255)),
                ("room", models.CharField(max_length=230, null=True)),
                ("address", django_google_maps.fields.AddressField(max_length=200)),
                (
                    "geolocation",
                    django_google_maps.fields.GeoLocationField(
                        blank=True, max_length=100, null=True
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="academics.course",
                    ),
                ),
            ],
        ),
    ]
