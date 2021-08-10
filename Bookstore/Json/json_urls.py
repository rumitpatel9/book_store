from django.urls import path,include
from rest_framework import routers
from . import json_views

router = routers.DefaultRouter()


router.register('register-data',json_views.Register_viewset)
router.register('contact-data',json_views.Contact_viewset)
router.register('books-data',json_views.Books_viewset)
router.register('bookscategories-data',json_views.BooksCategories_viewset)
router.register('cart-data',json_views.CART_viewset)
router.register('orderplacedetails-data',json_views.ORDER_PLACE_DETAILS_viewset)
router.register('blogcomments-data',json_views.Blog_Comments_viewset)

urlpatterns = [
    path('json/',include(router.urls))
]