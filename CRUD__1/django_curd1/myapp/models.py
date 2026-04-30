from django.db import models

# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=50)
    product_price=models.FloatField()
    product_qty=models.IntegerField()

    # def __str__(self):
    #     return f"{self.product_name} {self.product_price} {self.product_qty}"