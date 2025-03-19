from django.db import models


class SalesReport(models.Model):
    date = models.DateField(unique=True)
    total_sales = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00)
    total_orders = models.PositiveIntegerField(default=0)
    total_revenue = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sales Report - {self.date}"
