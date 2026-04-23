from django.shortcuts import render
from myapp.models import *
from myapp.serializer import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset=product.objects.all()
    serializer_class=ProductSerializer

    permission_classes=[IsAuthenticated]

    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_fields=["price","qty"]

    search_fields=['name']