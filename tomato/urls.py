from django.urls import path
from .views import *

app_name='tomato'

urlpatterns = [
    #register
    path('register/',user_register,name='reg'),
    #login
    path('login/',user_login,name='log'),
    #logout
    path('logout/',user_logout,name='logout'),
    #home
    path('home/',home),
    #restaurents
    path('restaurents/',restaurent_data,name='res'),
    #menus
    path('menu/<int:id>',menu,name='menu'),
    #profile
    path('userinfo/',userinfo,name='pro'),
    #buynow order
    path('buynow/<int:id>',buy_now,name='buynow'),
    #addtocart order
     path('addtocart/<int:id>',add_to_cart,name='addtocart'),
    #viewcart
    path('viewcart/',view_cart,name='viewcart'),
    #orders placed
    path('orders/<int:id>',orders,name='order'),
    #remove items
    path('remove/<int:id>/',remove_from_cart, name='remove_from_cart'),
    #hotel search
    path('search/',search_view,name='searchview'),
    #items search 
    path('itemssearchview/',item_search_view,name='itemsearchview'), 
    #success
    path('success/',success,name='succ')
]
