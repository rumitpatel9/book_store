from django.urls import path
from .product_views import *


urlpatterns = [
    path('',index, name ='home'),
    path('blog-details/',blog_details, name ='blog-details'),
    path('blog/',blog, name ='blog'),
    path('about/',about ,name ='about'),
    path('book-details/<bookid>/',single_book, name ='bookdetails'),
    path('books/',books_page ,name ='books'),
    path('Romantic/',romantic ,name ='Romance'),
    path('Drama/',drama,name ='Drama'),
]
