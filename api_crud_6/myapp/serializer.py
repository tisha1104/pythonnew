from rest_framework import serializers
from myapp.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'