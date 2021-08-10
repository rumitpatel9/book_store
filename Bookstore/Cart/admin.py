from django.contrib import admin
from .cart_models import *

# Register your models here.


class AdminCart(admin.ModelAdmin):
    list_display = ['user_id','book_image','book_name','book_price','quantity','total']


admin.site.register(Cart, AdminCart)


class AdminOrder(admin.ModelAdmin):
    list_display = ['user_id','order_id','date','qrcode']


admin.site.register(OrderPlaceDetails,AdminOrder)

