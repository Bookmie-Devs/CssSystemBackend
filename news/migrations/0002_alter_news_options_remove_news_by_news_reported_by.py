# Generated by Django 5.1.3 on 2024-12-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='by',
        ),
        migrations.AddField(
            model_name='news',
            name='reported_by',
            field=models.CharField(default='ss', max_length=100),
            preserve_default=False,
        ),
    ]