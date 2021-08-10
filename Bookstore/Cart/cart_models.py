from django.db import models

# Create your models here.
class Cart(models.Model):
    user_id = models.CharField(max_length=200)
    book_image = models.ImageField(upload_to='cart',blank=True)
    book_name = models.CharField(max_length=200)
    book_price = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)


class OrderPlaceDetails(models.Model):
    user_id = models.CharField(max_length=200)
    order_id = models.CharField(max_length=200)
    order_details = models.TextField()
    date = models.CharField(max_length=200,default='')
    qrcode = models.ImageField(default='', blank=True)
    total = models.IntegerField(default=0)
    TXNID = models.CharField(max_length=200, default='')
    paymentmode = models.CharField(max_length=200, default='')
    status = models.CharField(max_length=200, default='')
    BANKTXNID = models.CharField(max_length=200, default='')
    invoice = models.FileField(default='')


