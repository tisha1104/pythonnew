from rest_framework import serializers
from crud_app.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"