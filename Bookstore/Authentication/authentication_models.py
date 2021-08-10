from django.db import models

# Create your models here.


class Register(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_nu = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField()
    password = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200,default='')
    profile_image = models.ImageField(default='',blank=True,upload_to='profile_image')


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()