from django.shortcuts import render
from myapp.models import *
from myapp.seriaizer import *
from rest_framework.permissions import AllowAny ,IsAdminUser,IsAuthenticated
from rest_framework.decorators import api_view,APIView,action,permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
import razorpay
# Create your views here.

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def get_permissions(self):
        if self.action=='list':
            permission_classes=[AllowAny]
        elif self.action=='create':
            permission_classes=[AllowAny]
        elif self.action=='retrieve':
            permission_classes=[AllowAny]
        elif self.action=='destroy':
            permission_classes=[AllowAny]
        elif self.action=='update':
            permission_classes=[AllowAny]
        else :
            print(self.action)
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    def get_permissions(self):
        if self.action=='list':
            permission_classes=[AllowAny]
        elif self.action=='create':
            permission_classes=[AllowAny]
        elif self.action=='retrieve':
            permission_classes=[AllowAny]
        elif self.action=='destroy':
            permission_classes=[AllowAny]
        elif self.action=='update':
            permission_classes=[AllowAny]
        else :
            print(self.action)
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

class  ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get_permissions(self):
        if self.action=='list':
            permission_classes=[AllowAny]
        elif self.action=='create':
            permission_classes=[AllowAny]
        elif self.action=='retrieve':
            permission_classes=[AllowAny]
        elif self.action=='destroy':
            permission_classes=[AllowAny]
        elif self.action=='update':
            permission_classes=[AllowAny]
        else :
            print(self.action)
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
class AddressViewset(ModelViewSet):
    serializer_class=AddressSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class CartViewSet(ModelViewSet):
    serializer_class=CartItemSerializer
    permission_classes=[IsAuthenticated]

    def get_cart(self,user):
        cart,created = Cart.objects.get_or_create(user=user)
        return cart
    
    def list(self, request):
        cart= self.get_cart(request.user)
        serializer=CartSerializer(cart)
        return Response(serializer.data)
    

    @action(detail=False,methods=['POST'])
    def add(self,request):
        cart=self.get_cart(request.user)

        product_id= request.data.get('product')
        quantity= int(request.data.get('quantity',1))

        try:
            product= Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error":"Product not found"},status=404)
        
        item,created = CartItem.objects.get_or_create(cart=cart,product=product)

        if not created:
            item.quantity +=quantity
        else:
            item.quantity = quantity
        
        item.save()

        return Response({"message":"product added to caret"})


@api_view(['post'])
@permission_classes([IsAuthenticated])
def payment(request):
    amt=request.data['amount']
    client=razorpay.Client(auth=("rzp_test_SF5R7ur5nvvYLR", "NgUDBnx9JpMGHTWixBznB0S3"))   

    data={"amount":int(amt)*100,"currency":"INR","receipt":"order_recptid_11"}
    payment=client.order.create(data=data)

    return Response(payment)


@api_view(['post'])
@permission_classes([IsAuthenticated])
def create_order(request):
    user = request.user
    address = Address.objects.get(pk=request.data['address'])
    paymethod = request.data['paymethod']
    total = request.data['total_amount']

    order = Order.objects.create(user=user,address=address,total_amount=total,payment_method=paymethod)

    cart = Cart.objects.get(user=user)
    for c in cart.items.all():
        OrderItem.objects.create(order=order,product=c.product,price=c.product.price,quantity=c.quantity)
        c.delete()
    cart.delete()

    return Response({"message":"Order confirm"})