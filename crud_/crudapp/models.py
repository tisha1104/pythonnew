# from unicodedata import name
from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=20)

class Product(models.Model):
    categorie=models.ForeignKey(Categories,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    qty=models.IntegerField()
    image=models.ImageField(upload_to="image")

    def __str__(self):
        return self.name


