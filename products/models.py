from django.db import models
from uuid import uuid4
import secrets
import string

# Create your models here.

type_of_product = [
    ("cloth", "cloth"),
    ("books", "books"),
    ("utilities", "utilities"),
]


class Product(models.Model):
    product_id = models.UUIDField(
        default=uuid4, primary_key=True, unique=True, editable=False
    )
    product_image = models.ImageField(upload_to="products",null=True)
    product_name = models.CharField(max_length=255)
    type_of_product = models.CharField(max_length=255, choices=type_of_product)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


class ProductPayment(models.Model):
    payment_id = models.UUIDField(unique=True, primary_key=True, default=uuid4)
    reference = models.CharField(max_length=255, null=True, blank=True, editable=False)
    transaction_validation_code = models.CharField(max_length=100, unique=True)
    transaction = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    payed_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Payed")
    payment_successful = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product Payment"
        verbose_name_plural = "Product Payments"

        db_table = "product_payment"

    def generate_unique_validation_code(self):
        """Generate a unique 6-character transaction validation code."""
        while True:
            code = "".join(
                secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6)
            )
            # Check if the code is unique in the database
            if not ProductPayment.objects.filter(
                transaction_validation_code=code
            ).exists():
                return code

    def save(self, *args, **kwargs):
        if not self.transaction_validation_code:  # Only generate if not already set
            self.transaction_validation_code = self.generate_unique_validation_code()
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.transaction_validation_code)
