from django.urls import path
from .authentication_views import *
urlpatterns = [
    path('login/',login_page, name ='login'),
    path('register/',register_page, name ='register'),
    path('myaccount/',my_account_page, name ='myaccount'),
    path('contact/',contact_page, name ='contact'),
    path('logout/',logout_page ,name ='logout'),
    path('error404/',error_404_page ,name ='error'),
]
