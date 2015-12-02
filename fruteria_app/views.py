from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from forms import NewForm
from models import Order, Product, Order_item
@login_required
def index(request):
    pedidos = Order.objects.filter(user = request.user)
    data={
        'title_base':"Titulo Base",
        'pedidos':pedidos,
    }
    return render(request,"fruteria_app/index.html",data)

@login_required
def new(request):
    form = NewForm()
    data = {
        'form':form,
    }
    return render(request,"fruteria_app/new.html",data)


# Create your views here.
