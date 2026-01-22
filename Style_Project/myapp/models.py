from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="cat_image")

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    qty = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to="pro_image")
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qty=models.IntegerField()
  
    def get_total_price(self):
        return self.qty*self.product.price
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    data = models.DateField()
    total = models.FloatField()
    status = models.CharField(max_length=20,default="pending")
    paytype= models.CharField(max_length=20,default="online")
    payid = models.CharField(max_length=50)

class OrderDetials(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField()
    price=models.FloatField()
    