from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User



class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    stock = models.IntegerField(default=1)
    price = models.FloatField(default=0)

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Usuario')
    date_order = models.DateTimeField(auto_now=True)
    shipping_address = models.CharField(max_length=500)


class Order_item(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    qty = models.IntegerField(default=1)

