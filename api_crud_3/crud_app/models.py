from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    description=models.TextField()
    qty=models.IntegerField()
    image=models.ImageField(upload_to="product/",blank=True,null=True)
    
    def __str__(self):
        return self.name