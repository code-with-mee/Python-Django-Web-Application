from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from customers.models import Customer


class Order(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
