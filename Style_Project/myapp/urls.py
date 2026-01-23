from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',index,name='index'),
    path('jewellery/',jewellery,name='jewellery'),
    path('fashion/',fashion,name='fashion'),
    path('electronic/',electronic,name='electronic'),
    path("user-login",login_register,name='login_register'),
    path('user-regierstation',user_regierstation,name='user-regierstation'),
    path('user-logout',user_logout,name="user-logout"),
    path('cart/',cart_view, name='cart'),
    path('details',details,name="details"),
    path('getproducts',get_products,name="getproducts"),
    path('getcategories',get_categories,name="getcategories"),
    path('searchproduct',search_product,name="searchproduct"),
    path('addtocart',addtocart,name='addtocart'),
    path('removecart',removecart,name='removecart'),
    path('changeqty',changeqty,name='changeqty'),
    path("payment",payment,name="payment"),
    path('makeorder',makeorder,name='makeorder'),
    path('my-orders',my_orders, name='my_orders')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)