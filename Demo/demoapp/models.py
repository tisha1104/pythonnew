from django.db import models

# Create your models here.
class student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    age=models.PositiveIntegerField()

class course(models.Model):
   title=models.CharField(max_length=100)
   description=models.TextField()
   start_date=models.DateField()
   end_date=models.DateField()