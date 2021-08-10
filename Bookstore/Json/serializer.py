from rest_framework import serializers
from Authentication.authentication_models import *
from Product.product_models import *
from Cart.cart_models import *

class Register_data(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

class Contact_data(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields ='__all__'

class BooksCategories_data(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BooksCategories
        fields ='__all__'

class Books_data(serializers.ModelSerializer):
    class Meta:
        model =Books
        fields ='__all__'

class CART_data(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields ='__all__'

class ORDER_PLACE_DETAILS_data(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderPlaceDetails
        fields ='__all__'

class Blog_Comments_data(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogCommentPersonDetails
        fields ='__all__'