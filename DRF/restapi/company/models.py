from django.db import models

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=20)
    owner=models.CharField(max_length=20)



class Dept(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=20)
    hod=models.CharField(max_length=20)

class Emp(models.Model):
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    age=models.IntegerField()