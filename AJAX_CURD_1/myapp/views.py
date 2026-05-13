from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse,HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        phone=data.get('phone')
        Student.objects.create(name=name,email=email,phone=phone)
    return HttpResponse("Registraion Succesfully!")

def display(request):
    student=Student.objects.all()
    return JsonResponse({"student":list(student.values())})

def delete_student(request):
    sid=request.GET['sid']
    st=Student.objects.get(pk=sid)
    st.delete()
    return HttpResponse("Student Recoerd Deleted")

def getbyid(request):
    sid=request.GET['sid']
    st=Student.objects.filter(pk=sid)
    return  JsonResponse({"student":list(st.values())})

def update_student(request):
    if request.method=='POST':
        data=request.POST
        id=data.get('id')
        name=data.get('name')
        email=data.get('email')
        phone=data.get('phone')
        st=Student.objects.get(pk=id)
        st.name=name
        st.email=email
        st.phone=phone
        st.save()
    return HttpResponse("Student Recoerd Update Succesfully!")