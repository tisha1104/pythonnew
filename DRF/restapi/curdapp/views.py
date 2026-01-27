from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from curdapp.models import *
from curdapp.serializer import *
# Create your views here.

@api_view(['GET'])
def view_student(request):
    students=Student.objects.all()
    ser=StudentSerilaizer(students,many=True)
    return Response({"data":ser.data})

@api_view(['POST'])
def add_student(request):
    stdata=request.data
    ser=StudentSerilaizer(data=stdata)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"Something Went Wrong!"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Data Inserted Suceessfully:-"})
    
@api_view(['GET'])
def view_byid(request,id):
    student=Student.objects.get(pk=id)
    ser=StudentSerilaizer(student)
    return Response({"data":ser.data})

@api_view(['PUT'])
def update_student(request,id):
    sdata=request.data
    cdata=Student.objects.get(pk=id)
    ser=StudentSerilaizer(cdata,sdata,partial=True)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"Something Went Wrong!"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Data Updated Suceessfully:-"})
    

@api_view(['DELETE'])
def delete_student(request,id):
    sdata= Student.objects.get(pk=id)
    sdata.delete()
    return Response({"message":"Data Deleted Successfully!"})

