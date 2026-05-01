from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    emial=models.EmailField()
    sub=models.CharField(max_length=100)
    image=models.ImageField(upload_to="image",blank=True,null=True,default="test.png")
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)