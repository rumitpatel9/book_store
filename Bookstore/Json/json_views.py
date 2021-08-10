from django.shortcuts import render
from rest_framework import viewsets
from . import serializer
from Authentication.authentication_models import *
from Product.product_models import *
from Cart.cart_models import *

# Create your views here.

class Register_viewset(viewsets.ModelViewSet):
    queryset =Register.objects.all()
    serializer_class = serializer.Register_data


class Contact_viewset(viewsets.ModelViewSet):
    queryset =Contact.objects.all()
    serializer_class = serializer.Contact_data

class BooksCategories_viewset(viewsets.ModelViewSet):
    queryset =BooksCategories.objects.all()
    serializer_class = serializer.BooksCategories_data

class Books_viewset(viewsets.ModelViewSet):
    queryset =Books.objects.all()
    serializer_class = serializer.Books_data

class CART_viewset(viewsets.ModelViewSet):
    queryset =Cart.objects.all()
    serializer_class = serializer.CART_data

class ORDER_PLACE_DETAILS_viewset(viewsets.ModelViewSet):
    queryset =OrderPlaceDetails.objects.all()
    serializer_class = serializer.ORDER_PLACE_DETAILS_data

class Blog_Comments_viewset(viewsets.ModelViewSet):
    queryset =BlogCommentPersonDetails.objects.all()
    serializer_class = serializer.Blog_Comments_data
