from rest_framework import serializers
from company.models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'


class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dept
        fields='__all__'


    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['company']=CompanySerializer(instance.company).data
        return resp

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__' 
        

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['dept']=DeptSerializer(instance.dept).data
        return resp