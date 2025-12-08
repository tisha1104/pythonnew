from django.shortcuts import render,redirect
from myapp.models import product

# Create your views here.
def home(request):
    return render(request,"home.html")

def register_student(request):
    pid=request.POST.get('pid')
    name=request.POST.get('product_name')
    price=request.POST.get('product_price')
    qty=request.POST.get('product_qty')

    if not pid :
        product.objects.create(product_name=name,product_price=price,product_qty=qty)
        return render(request,'home.html',{'success':'Product registered successfully'})
    else:
        pr = product.objects.get(pk=pid)
        pr.product_name=name
        pr.product_price=price
        pr.product_qty=qty
        pr.save()
        return render(request,'home.html',{'success':'Product update successfully',})

def display(request):
    prod=product.objects.all()
    return render(request,"display.html",{"product":prod})

def delete_product(request):
    pid = request.GET.get("id")
    pr = product.objects.get(pk=pid)
    pr.delete()
    return redirect("display")

def edit_product(request):
    pid = request.GET.get("id")
    pr = product.objects.get(pk=pid)
    return render(request,"home.html",{"pr":pr})