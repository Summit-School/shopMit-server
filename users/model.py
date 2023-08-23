from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    password = models.CharField()
    validation = models.BooleanField(default=False)
    user_validation_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.user_name

    groups = models.ManyToManyField('auth.Group', related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_users', blank=True)

    class Meta:
        app_label = 'users'