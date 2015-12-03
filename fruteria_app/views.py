from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from forms import *
from models import Order, Product, Order_item
from django.shortcuts import get_object_or_404

@login_required
def index(request):
    pedidos = Order.objects.filter(user = request.user)
    data={
        'title_base':"Titulo Base",
        'pedidos':pedidos,
    }
    return render(request,"fruteria_app/index.html",{})

@login_required
def newProduct(request, product_id=None):
    if product_id!=None:
        product=get_object_or_404(Product,pk=product_id)
    else:
        product=Product()
        product.seller=request.user
    form = ProductForm(instance=product)
    data = {
        'form':form,
    }
    if request.method=='POST':
        form=ProductForm(request.POST, instance = product)
        if form.is_valid():
            product = form.save(commit=False)

            product.save()
            return render(request,"fruteria_app/index.html")
        else:
            data['form']=form
    return render(request,"fruteria_app/new.html",data)

@login_required
def newType(request, type_id=None):
    if type_id !=None:
        type=get_object_or_404(ProductType,pk=type_id)
    else:
        type=ProductType()

    form = TypeForm(instance=type)
    data = {
        'form':form,
    }
    if request.method=='POST':
        form = TypeForm(request.POST, instance=type)
        if form.is_valid():
            type=form.save(commit=False)
            type.save()
            return render(request,"fruteria_app/index.html")
        else:
            data['form']=form
            return render(request,"fruteria_app/new.html",data)
    return render(request,"fruteria_app/new.html",data)

@login_required
def newUnitType(request, unit_type_id = None):
    if unit_type_id!=None:
        unit_type = get_object_or_404(Unit_Type,pk=unit_type_id)
    else:
        unit_type = Unit_Type()
    form = UnitTypeForm(instance=unit_type)
    data = {
        'form':form,
    }
    if request.method=='POST':
        form = UnitTypeForm(request.POST, instance=unit_type)
        if form.is_valid():
            unit_type = form.save(commit=False)
            unit_type.save()
            return render(request,"fruteria_app/index.html")
        else:
            data['form']=form
    return render(request,"fruteria_app/new.html",data)

@login_required
def newOrder(request, order_id = None):
    form = OrderForm(instance=order_id)
    data = {
        'form':form,
    }
    return render(request,"fruteria_app/new.html",data)


# Create your views here.
