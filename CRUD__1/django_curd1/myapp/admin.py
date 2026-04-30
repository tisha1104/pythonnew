from django.contrib import admin
from myapp.models import *
# Register your models here.

class productadmin(admin.ModelAdmin):
    list_display=('product_name','product_price','product_qty')

admin.site.register(product,productadmin)