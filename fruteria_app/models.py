from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User





class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Usuario')
    date_order = models.DateTimeField('Fecha de la Orden', auto_now=True )
    shipping_address = models.CharField('Direccion de envio', max_length=500)

class ProductType(models.Model):
    name = models.CharField('Tipo', max_length=200, blank=False)
    def __unicode__(self):
        return self.name


class Unit_Type(models.Model):
    name = models.CharField('Tipo de Unidad', max_length=200, blank=False)
    def __unicode__(self):
        return self.name




class Product(models.Model):
    name = models.CharField('Nombre', max_length=200, blank=False)
    description = models.CharField('Descripcion', max_length=200)
    stock = models.IntegerField('Cantidad en Stock', default=1)
    price_per_unit = models.FloatField('Precio por unidad',default=0, blank=False)
    type = models.ForeignKey(ProductType, verbose_name='Tipo de producto', blank=False)
    unit = models.ForeignKey(Unit_Type, verbose_name='Tipo de Unidad', blank=False)
    seller = models.ForeignKey(User, verbose_name='Vendedor')

class Order_item(models.Model):
    order = models.ForeignKey(Order,verbose_name='Orden')
    product = models.ForeignKey(Product, verbose_name='Producto')
    qty = models.IntegerField('Cantidad', default=1)
    user = models.ForeignKey(User, verbose_name='Usuario')