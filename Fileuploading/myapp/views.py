from django.shortcuts import render
from myapp.models import *
# Create your views here.

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        pro=Product.objects.create(name=name)
        files=request.FILES.getlist("file")
        for f in files:
            Images.objects.create(product=pro,image=f)

    products=Product.objects.all()        
    return render(request,"index.html",{"products":products})