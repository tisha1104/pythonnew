from crudapp.models import Product
from crudapp.models import Categories
from django.shortcuts import render,redirect
from crudapp.models import *
# Create your views here.
def home(request):
    product=Product.objects.all()
    category=Categories.objects.all()
    if request.method=='POST':
        cat=request.POST['cat']
        name=request.POST['name']
        price=request.POST['price']
        qty=request.POST['qty']
        photo=request.FILES['photo']
        categories=Categories.objects.get(pk=cat)
        Product.objects.create(name=name,price=price,qty=qty,image=photo,categorie=categories)
        return render(request,"home.html",{"msg":"Prtoduct Ragistered!","category":category,"product":product})
    else:
        return render(request,"home.html",{"category":category,"product":product})

def delete_product(request):
    id=request.GET['id']
    prod=Product.objects.get(pk=id)
    prod.delete()
    return redirect("home")

def edit_product(request):
    product=Product.objects.all()
    category=Categories.objects.all()
    if request.method==['POST']:
        cat=request.POST['cat']
        id=request.POST['id']
        name=request.POST['name']
        price=request.POST['price']
        qty=request.POST['qty']

        prod=Product.objects.get(pk=id)
        