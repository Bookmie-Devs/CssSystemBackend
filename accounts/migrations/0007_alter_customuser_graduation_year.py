# Generated by Django 4.2.7 on 2024-12-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_customuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='graduation_year',
            field=models.IntegerField(),
        ),
    ]
