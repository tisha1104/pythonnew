from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import *
from myapp.serailazer import *
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import FormParser,MultiPartParser
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny


# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    permission_classes =[IsAuthenticated]
    
    # parser_classes=[MultiPartParser,FormParser]
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_fields=["price","qty"]

    search_fields=['name','description']