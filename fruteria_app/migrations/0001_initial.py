# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_order', models.DateTimeField(auto_now=True, verbose_name=b'Fecha de la Orden')),
                ('shipping_address', models.CharField(max_length=500, verbose_name=b'Direccion de envio')),
                ('user', models.ForeignKey(verbose_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField(default=1, verbose_name=b'Cantidad')),
                ('order', models.ForeignKey(verbose_name=b'Orden', to='fruteria_app.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Nombre')),
                ('description', models.CharField(max_length=200, verbose_name=b'Descripcion')),
                ('stock', models.IntegerField(default=1, verbose_name=b'Cantidad en Stock')),
                ('price_per_unit', models.FloatField(default=0, verbose_name=b'Precio por unidad')),
                ('seller', models.ForeignKey(verbose_name=b'Vendedor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Unit_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Tipo de Unidad')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(verbose_name='Tipo de producto', to='fruteria_app.ProductType'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(verbose_name=b'Tipo de Unidad', to='fruteria_app.Unit_Type'),
        ),
        migrations.AddField(
            model_name='order_item',
            name='product',
            field=models.ForeignKey(verbose_name=b'Producto', to='fruteria_app.Product'),
        ),
        migrations.AddField(
            model_name='order_item',
            name='user',
            field=models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
