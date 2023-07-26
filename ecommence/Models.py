from django.db import models
from django.contrib.auth.models import AbstractUser

class Product (models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7,decimal_places=3)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    user_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    validation = models.BooleanField(default=False)
    user_validation_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.user_name
