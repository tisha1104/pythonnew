from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField()

    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    data = models.DateField()
    total = models.FloatField()
    status = models.CharField(max_length=20,default="pending")
    paytype= models.CharField(max_length=20,default="online")
    payid = models.CharField(max_length=50)
    address=models.ForeignKey(Address,on_delete=models.CASCADE,null=True)

class OrderDetials(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE, related_name="details")
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField()
    price=models.FloatField()
    

    def total_price(self):
        return self.price*self.qty
    
class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image',null=True,blank=True)

    def __str__(self):
        return self.user.username
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField() 
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.rating}{self.message}{self.created_at}"