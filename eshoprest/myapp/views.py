from django.shortcuts import render
from myapp.models import *
from myapp.seriaizer import *
from rest_framework.permissions import AllowAny ,IsAdminUser,IsAuthenticated
from rest_framework.decorators import api_view,APIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def get_permissions(self):
        if self.action=='list':
            permission_classes=[AllowAny]
        elif self.action=='create':
            permission_classes=[AllowAny]
        elif self.action=='retrieve':
            permission_classes=[AllowAny]
        elif self.action=='destroy':
            permission_classes=[AllowAny]
        elif self.action=='update':
            permission_classes=[AllowAny]
        else :
            print(self.action)
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    def get_permissions(self):
        if self.action=='list':
            permission_classes=[AllowAny]
        elif self.action=='create':
            permission_classes=[AllowAny]
        elif self.action=='retrieve':
            permission_classes=[AllowAny]
        elif self.action=='destroy':
            permission_classes=[AllowAny]
        elif self.action=='update':
            permission_classes=[AllowAny]
        else :
            print(self.action)
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

class  ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get_permissions(self):
        if self.action=='list':
            permission_classes=[AllowAny]
        elif self.action=='create':
            permission_classes=[AllowAny]
        elif self.action=='retrieve':
            permission_classes=[AllowAny]
        elif self.action=='destroy':
            permission_classes=[AllowAny]
        elif self.action=='update':
            permission_classes=[AllowAny]
        else :
            print(self.action)
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]