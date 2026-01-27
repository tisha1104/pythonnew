from rest_framework import serializers
from curdapp.models import *

class StudentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"