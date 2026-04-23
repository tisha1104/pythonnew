from django.shortcuts import render
from crud_app.models import *
from crud_app.serializer import *
from rest_framework  import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.parsers import MultiPartParser,FormParser

# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get_permissions(self):
        if self.action in ['create','destory']:
            return[IsAdminUser()]
        return [IsAuthenticated()]
    
    parser_classes=[MultiPartParser,FormParser]

    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_fields=["price","qty"]
    search_fields=['name','description']