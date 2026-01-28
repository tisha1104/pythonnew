from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView,permission_classes
from company.models import *
from company.serializer import *
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
# Create your views here.


class DeptApi(APIView):

    def get(self,request):
        depts=Dept.objects.all()
        ser=DeptSerializer(depts,many=True)
        return Response({"data":ser.data})
    
    def post(self,request):
        ser=DeptSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors})
        else:
            ser.save()
            return Response({"data":ser.data})
        

class DeptupdateAPI(APIView):

    def get(self,request,id):
        dept=Dept.objects.get(pk=id)
        ser=DeptSerializer(dept)
        return Response({"data":ser.data})
    
    def delete(self,request,id):
        dept=Dept.objects.get(pk=id)
        dept.delete()
        return Response({"message":"dept deleted!"})
    
    def put(self,request,id):
        dept=Dept.objects.get(pk=id)
        ser=DeptSerializer(dept,request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors})
        else:
            ser.save()
            return Response({"data":ser.data})
        
@api_view(['POST'])
def addEmp(request,id):
    data=request.data
    data.update({"dept":id})
    ser=EmpSerializer(data=data)
    if not ser.is_valid():
        return Response({"errors":ser.errors})
    else:
        ser.save()
        return Response({"data":ser.data})
    
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getemps(request):
        emps=Emp.objects.all()
        ser=EmpSerializer(emps,many=True)
        return Response({"data":ser.data})



@api_view(['PUT'])
def updateEmp(request,id,eid):
    data=request.data
    data.update({"dept":id})
    cdata=Emp.objects.get(pk=eid)
    ser=EmpSerializer(cdata,data)
    if not ser.is_valid():
        return Response({"errors":ser.errors})
    else:
        ser.save()
        return Response({"data":ser.data})
    



class EmpById(APIView):
    

    def get(self,request,id):
        emp=Emp.objects.get(pk=id)
        ser =EmpSerializer(emp)
        return Response({"data":ser.data})

    def delete(self,request,id):
        emp=Emp.objects.get(pk=id)
        emp.delete()
        return Response({"message":"Empoyee Deleted!"})