from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[
        ('Admin', 'Admin'),
        ('Cashier', 'Cashier'),
        ('Manager', 'Manager'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
