from django.shortcuts import render
from myapp.models import *
from pathlib import Path
# Create your views here.

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        pro=Product.objects.create(name=name)
        files=request.FILES.getlist("file")
        for f in files:
            extension= Path(f.name).suffix
            if extension=='.png':
                Images.objects.create(product=pro,image=f)

    products=Product.objects.all()        
    return render(request,"index.html",{"products":products})