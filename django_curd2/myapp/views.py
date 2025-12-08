from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def home(request):
    Products = product.objects.all()
    if request.method=='POST':
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']
        product.objects.create(name=name,price=price,qty=qty)
        return render(request,"home.html",{"Products":Products})
    else:
        return render(request,"home.html",{"Products":Products})

def delete_product(request):
    id = request.GET['id']
    prod = product.objects.get(pk=id)
    prod.delete()
    return redirect("home")

def edit_product(request):
    Products = product.objects.all()
    if request.method=='POST':
        id = request.POST['id']
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']

        prod= product.objects.get(pk=id)
        prod.name=name
        prod.price=price
        prod.qty=qty
        prod.save()
        return render(request,"home.html",{"Products":Products})
    else:
        id = request.GET['id']
        prod = product.objects.get(pk=id)
        return render(request,"home.html",{"prod":prod,"Products":Products})


