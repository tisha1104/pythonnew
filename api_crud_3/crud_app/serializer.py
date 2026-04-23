from rest_framework import serializers
from crud_app.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"