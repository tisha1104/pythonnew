from rest_framework import serializers
from crud_app.models import *

class StudentSerializer(serializers.ModelSerializer):
    class meta:
        model:Student
        fildes="__all__"