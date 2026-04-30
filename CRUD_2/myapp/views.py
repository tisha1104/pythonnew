from django.shortcuts import render,redirect
from myapp.models import * 
# Create your views here.
def home(request):
    product=Product.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        qty=request.POST['qty']
        image=request.FILES['image']
        Product.objects.create(name=name,price=price,qty=qty,image=image)
        return render(request,"home.html",{"msg":"Product Register Done!","product":product})
    else:
        return render(request,"home.html",{"product":product})
    

def delete_student(request):
    id=request.GET['id']
    p=Product.objects.get(pk=id)
    p.delete()
    return redirect("home")

def edit_student(request):
    product=Product.objects.all()
    if request.method=='POST':
        id=request.GET['id']
        name=request.POST['name']
        price=request.POST['price']
        qty=request.POST['qty']
        p=Product.objects.get(pk=id)
        p.name=name
        p.price=price
        p.qty=qty
        if request.FILES:
            p.image=request.FILE['image']
        p.save()
        return redirect("home")
    else:
        id=request.GET['id']
        p=Product.objects.get(pk=id)
        return render(request,"home.html",{"product":product,"p":p})