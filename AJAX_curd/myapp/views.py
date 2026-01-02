from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse ,HttpResponse
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        data= request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        student.objects.create(name=name,email=email,phone=phone)

        return HttpResponse("Registration Successfully!")
    
def display(request):
    studentes=student.objects.all()
    return JsonResponse({"studentes":list(studentes.values())})

def delete_student(request):
    sid=request.GET['sid']
    st=student.objects.get(pk=sid)
    st.delete()
    return HttpResponse("Student Record Deleted Succesfully!") 

def getbyid(request):
    sid=request.GET['sid']
    st=student.objects.filter(id=sid)
    return JsonResponse({"studentes":list(st.values())}) 

def update_student(request):
      if request.method=='POST':
        data= request.POST
        id=data.get('id')
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        st=student.objects.get(pk=id)
        st.name=name
        st.email=email
        st.phone=phone
        st.save()
        return HttpResponse("Student Reoerd Updaeted Successfully!")
      

def search(request):
    value=request.GET['value']
    studentes=student.objects.filter(Q(name__startswith=value)|Q(email__startswith=value)|Q(phone__startswith=value))

    return JsonResponse({"studentes":list(studentes.values())})