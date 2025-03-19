from django.db import models
# Import Category from the categories app
from categories.models import Category
import uuid


class Product(models.Model):
    name = models.CharField(max_length=200)
    # Auto-generate unique SKU
    sku = sku = models.CharField(
        max_length=100, unique=True, default=uuid.uuid4)
    barcode = models.CharField(
        max_length=100, unique=True, blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
