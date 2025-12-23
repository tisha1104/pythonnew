from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from django.http import JsonResponse 
# Create your views here.

def index(request):    
    return render(request,"index.html")

def view(request):
    data= request.GET['data']
    products=product.objects.filter(name__startswith=data)
    return JsonResponse({"products":list(products.values())})

def countries(request):
    countries= country.objects.all()
    return JsonResponse({"countries":list(countries.values())})