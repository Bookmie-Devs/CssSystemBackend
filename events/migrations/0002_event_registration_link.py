# Generated by Django 4.2.7 on 2025-01-05 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='registration_link',
            field=models.URLField(blank=True, help_text='Registration link for event if any', null=True),
        ),
    ]
