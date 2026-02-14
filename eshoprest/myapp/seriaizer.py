from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
Category, Product, Address,
Cart, CartItem,
Order, OrderItem
)

# ---------------- User ----------------

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
# ---------------- Category ----------------

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# ---------------- Product ----------------

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
    queryset=Category.objects.all(),
    source='category',
    write_only=True
    )


    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description',
            'price', 'stock', 'image',
            'is_available', 'created_at',
            'category', 'category_id'
        ]


# ---------------- Address ----------------

class AddressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    

    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ['user', 'created_at']


# ---------------- Cart Item ----------------

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
    queryset=Product.objects.all(),
    source='product',
    write_only=True
    )
    total_price = serializers.SerializerMethodField()


    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'product_id', 'quantity', 'total_price']

def get_total_price(self, obj):
    return obj.total_price()


# ---------------- Cart ----------------

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)


    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items']


# ---------------- Order Item ----------------

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)


    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price', 'sub_total']

    sub_total = serializers.SerializerMethodField()

    def get_sub_total(self, obj):
        return obj.sub_total()


# ---------------- Order ----------------

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    order_items = OrderItemSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)
    address_id = serializers.PrimaryKeyRelatedField(
    queryset=Address.objects.all(),
    source='address',
    write_only=True
    )


    class Meta:
        model = Order
        fields = [
            'id', 'user', 'address', 'address_id',
            'total_amount', 'status', 'payment_method',
            'created_at', 'order_items'
        ]