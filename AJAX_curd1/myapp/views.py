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

def delete_student(request):
    sid=request.GET['sid']
    st=student.objects.get(pk=sid)
    st.delete()
    return HttpResponse("Student Recoerd Delete Suceecssfully!")

def getbyid(request):
    sid=request.GET['sid']
    st=student.objects.filter(id=sid)
    return JsonResponse({"studentes":list(st.values())})