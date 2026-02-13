from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# ---------------- Category ----------------

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# ---------------- Product ----------------

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock', 'is_available', 'created_at')
    list_filter = ('category', 'is_available')
    search_fields = ('name',)
    list_editable = ('price', 'stock', 'is_available')

# ---------------- Address ----------------

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'city', 'state', 'pincode', 'phone')
    search_fields = ('full_name', 'city', 'pincode')

# ---------------- Cart ----------------

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')

# ---------------- Cart Item ----------------

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity')
    list_filter = ('product',)

# ---------------- Order ----------------

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'status', 'payment_method', 'created_at')
    list_filter = ('status', 'payment_method')
    search_fields = ('user__username',)
    inlines = [OrderItemInline]

# ---------------- Order Item ----------------

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')