from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid
from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from customers.models import Customer


class Order(models.Model):
    order_number = models.CharField(
        max_length=100, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    ]
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order_number)  # ✅ Convert UUID to string

    def update_total(self):
        """ Update total amount based on all order items """
        total = sum(item.subtotal for item in self.orderitem_set.all())
        self.total_amount = total
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


# Signal to reduce stock


@receiver(post_save, sender=OrderItem)
def reduce_stock(sender, instance, created, **kwargs):
    """ Reduce product stock when an order item is created """
    if created:
        instance.product.stock -= instance.quantity
        instance.product.save()
