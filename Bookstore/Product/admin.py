from django.contrib import admin
from .product_models import *
# Register your models here.
admin.site.register(BlogCommentPersonDetails)


class MembarCategories(admin.ModelAdmin):
    list_display = ['categories_name']


admin.site.register(BooksCategories, MembarCategories)


class MembarProducts(admin.ModelAdmin):
    list_display = ['books_data','book_image','book_name','book_offer_price',
                    'book_author_name' ,'book_actual_price','book_publisher','book_language','book_total_pages','book_published_year']
    list_filter = ['books_data','book_name','book_publisher', 'book_author_name','book_published_year']


admin.site.register(Books, MembarProducts)