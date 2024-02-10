from collections.abc import Collection
from django.db import models
from django.conf import settings
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name


class Item(models.Model):
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item.name


class Customers(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.ManyToManyField(Item, through='Orders')

    def __str__(self):
        return self.owner.username

class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('customer', 'product'),)

    def __str__(self):
        return f'User : ({self.customer.owner.username}) Product: ({self.product.item.name})'



class Info(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=200)
    postal_code = models.IntegerField()
    state = models.CharField(max_length=100)
