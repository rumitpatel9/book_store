from django.urls import path
from .cart_views import *
urlpatterns = [
    path('Cart/',cart_page, name ='cart'),
    path('add-to-cart/<book_id>/',add_to_cart, name ='cartdetails'),
    path('delete-cart-product/<book_id>/',delete_cart_product,name ='delete'),
    path('Check-Out/', checkout_page, name='checkout'),
    path('compare/',compare_page ,name ='compare'),
    path("handlerequest/", handlerequest, name="HandleRequest"),
]
