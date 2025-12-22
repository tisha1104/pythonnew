from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def home(request):
    Products = product.objects.all()
    category = Category.objects.all()
    if request.method=='POST':
        cat = request.POST['cat']
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']
        image = request.FILES['image']
        categories =  Category.objects.get(pk=cat)
        product.objects.create(name=name,price=price,qty=qty,image=image,Category=categories)
        return render(request,"home.html",{"Products":Products,"category":category})
    else:
        return render(request,"home.html",{"Products":Products,"category":category})

def delete_product(request):
    id = request.GET['id']
    prod = product.objects.get(pk=id)
    prod.delete()
    return redirect("home")

def edit_product(request):
    Products = product.objects.all()
    category = Category.objects.all()

    if request.method=='POST':
        cat = request.POST['cat']
        id = request.POST['id']
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']

        prod= product.objects.get(pk=id)
        prod.name=name
        prod.price=price
        prod.qty=qty
        prod.Category = Category.objects.get(pk=cat)
        if request.FILES:
            prod.image = request.FILES['image']
        prod.save()
        return render(request,"home.html",{"Products":Products,"category":category})
    else:
        id = request.GET['id']
        prod = product.objects.get(pk=id)
        return render(request,"home.html",{"prod":prod,"Products":Products,"category":category})


