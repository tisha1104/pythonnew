from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from myapp.models import *
from myapp.serializers import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer