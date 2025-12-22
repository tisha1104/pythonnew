from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class product(models.Model):
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to="image",default="test.png")