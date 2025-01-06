from django.db import models
from uuid import uuid4
# Create your models here.

type_of_product = [("cloth", "cloth"), ("books", "books"), ("utilities", "utilities"),]

class Product(models.Model):
    product_id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    product_name = models.CharField(max_length=255)
    type_of_product = models.CharField(max_length=255, choices=type_of_product)
    price = models.DecimalField(decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
