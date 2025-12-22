from django.db import models

# Create your models here.

class product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.ImageField()
    image=models.ImageField(upload_to="image",default="test.png")