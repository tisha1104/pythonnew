from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import *
from myapp.serilalizer import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework.parsers import MultiPartParser,FormParser
# Create your views here.

class Productviewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSeriailzer
    def get_permissions(self):
        if self.action in['create','destroy']:
            return[AllowAny()]
            # return [IsAdminUser()]
        return [IsAuthenticated()]
     
    parser_classes=[MultiPartParser,FormParser]
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filter_fileds=['price',"qty"]

    search_fileds=["name","description"]