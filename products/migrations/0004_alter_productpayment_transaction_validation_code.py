# Generated by Django 5.1.4 on 2025-01-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_productpayment_payment_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productpayment",
            name="transaction_validation_code",
            field=models.CharField(editable=False, max_length=100, unique=True),
        ),
    ]
