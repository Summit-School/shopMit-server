from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=3)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'products'
