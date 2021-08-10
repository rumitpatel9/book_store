from django.contrib import admin
from .authentication_models  import *
# Register your models here.

class RegisterMembersData(admin.ModelAdmin):
    list_display = ['user_id','first_name','last_name','email','mobile_nu','country', 'address','city','state','pincode','password']
    list_filter = ['country','city','state']


admin.site.register(Register, RegisterMembersData)


class ContactMembersData(admin.ModelAdmin):
    list_display = ['name','email','subject','message']
    list_filter = ['name','subject']


admin.site.register(Contact, ContactMembersData)
