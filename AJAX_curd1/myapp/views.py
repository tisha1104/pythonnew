from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse, HttpResponse
# Create your views here.


def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        phone=data.get('phone')

        student.objects.create(name=name,email=email,phone=phone)

        return HttpResponse("Ragistration Successfully!")
    
def display(request):
    studentes=student.objects.all()
    return JsonResponse({"studentes":list(studentes.values())})