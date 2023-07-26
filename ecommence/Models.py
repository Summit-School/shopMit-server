# ecommerce/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    user_validation = models.BooleanField(default=False)
    user_validation_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.username
