from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.

def index(request):
    products = Product.objects.all()
    if request.method =='POST':
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']
        image = request.FILES['image']
        Product.objects.create(name=name,price=price,qty=qty,image=image)
        return render(request,"index.html",{"success":"Product Insert Succesfully","products":products})
    else:
        return render(request,"index.html",{"products":products})
    
def delete_product(request):
    id = request.GET['id']
    p = Product.objects.get(pk=id)
    p.delete()
    return redirect("index")

def edit_product(request):
    products = Product.objects.all()
    if request.method =='POST':
        id= request.POST.get('id')
        name= request.POST.get('name')
        qty= request.POST.get('qty')

        p= Product.objects.get(pk=id)
        p.name=name
        p.qty=qty
        if request.FILES:
            p.image = request.FILES['image']
        p.save()
        return render(request,"index.html",{"products":products})
    else:
        id= request.GET['id']
        p= Product.objects.get(pk=id)
        return render(request,"index.html",{"p":p,"products":products})