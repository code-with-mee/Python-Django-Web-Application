from django.db import models


class SalesReport(models.Model):
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_orders = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.date)
