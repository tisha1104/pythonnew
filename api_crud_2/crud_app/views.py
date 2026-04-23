
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from crud_app.models import *
from crud_app.serializer import *
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_student(request):
    students = Student.objects.all()
    ser = StudentSerializer(students, many=True)
    return Response({"data": ser.data})

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_student(request):
    stdata=request.data
    ser=StudentSerializer(data=stdata)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"Something went Wrong!"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"inserted succesfully!"})
    
@api_view(['GET'])
@permission_classes([AllowAny])
def view_byid(request,id):
    student=Student.objects.get(pk=id)
    ser=StudentSerializer(student)
    return Response({"data":ser.data})

@api_view(['PUT'])
def udate_student(request,id):
    sdata=request.data
    cdata=Student.objects.get(pk=id)
    ser=StudentSerializer(cdata,sdata,partial=True)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"Something went Wrong!"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"update succesfully!"})
    
@api_view(['DELETE'])
def delete_student(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return Response({"message":"Data Deleted"})