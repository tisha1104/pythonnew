from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=20)

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    image=models.ImageField(upload_to="image",validators=[FileExtensionValidator(allowed_extensions=['png'])])