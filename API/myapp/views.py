from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes 
from myapp.models import Product
from myapp.serializer import *
from rest_framework.parsers import MultiPartParser, FormParser
@api_view(['POST'])
def addproduct(request):
    data = request.data.copy()  
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data})
    return Response({"errors": serializer.errors}, status=400)

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()  
    serializer = ProductSerializer(products, many=True)
    return Response({"data": serializer.data})

@api_view(["PUT"])
@parser_classes([MultiPartParser, FormParser])
def update_student(request,id):
    sdata=request.data
    cdata=Product.objects.get(pk=id)
    ser=ProductSerializer(cdata,data=sdata)
    if ser.is_valid():
        ser.save()
        return Response({'data':ser.data,'message':'update successfully..'})
    else:
        return Response({'errors':ser.errors,'message':'something is went wrong..'})