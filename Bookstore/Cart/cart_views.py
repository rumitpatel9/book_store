from django.shortcuts import render,get_object_or_404,redirect
from Authentication.authentication_models import Register
from Product.product_models import Books
from .cart_models import *
from . import Checksum
import qrcode
import datetime
from django.views.decorators.csrf import csrf_exempt

MERCHANT_KEY ='IDoIr_ezOtgs_Xw0'
MERCHANT_ID = 'ESIrPr70117430282888'
# Create your views here.


def create_order_id():  # create orderid....
    import random
    random_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    order_id = ''.join(random.sample(random_string, 15))
    return order_id


def qr_code(message,order_id):  # create a order QR Code....
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(message)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'media/qrcode/{order_id}.png')


def cart_page(request):  # cart page...
    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register, user_id=request.session['user_id'])
        cart_products = Cart.objects.filter(user_id =request.session['user_id'])
        total = 0
        for cart_product in cart_products:
            total = float(cart_product.book_price) + total
        return render(request, 'Cart/cart.html',{'data':current_user,'cart_product':cart_products,'a':total})
    else:
        return render(request,'Cart/cart.html')


def add_to_cart(request, book_id):
    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register, user_id=request.session['user_id'])
        Userid = current_user.user_id
        cart_book_details = get_object_or_404(Books, pk= book_id)
        Book_Image = cart_book_details.book_image
        Book_Name = cart_book_details.book_name
        Book_Price = cart_book_details.book_offer_price
        Cart(user_id=Userid, book_image=Book_Image, book_name=Book_Name, book_price=Book_Price).save()
        return redirect('cart')
    else:
        return redirect('login')


def delete_cart_product(request,book_id):
    cart_book_details =get_object_or_404(Cart,pk = book_id)
    cart_book_details.delete()
    return redirect('cart')

def checkout_page(request):
    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register, user_id = request.session['user_id'])
        user_id =current_user.user_id
        email = current_user.email
        ###for a billing perpose..
        cart_products =Cart.objects.filter(user_id =request.session['user_id'])
        total =0
        for cart_product in cart_products:
            total = float(cart_product.book_price) + total
        gst_price = (total * (18 / 100))
        total = total + (gst_price)

        ###if user place the order then below function run...
        if request.method =='POST':
            order_id = create_order_id()
            name = request.POST['firstname'] + request.POST['lastname']
            address = request.POST['address']
            city = request.POST['city']
            email = request.POST['email']
            phone = request.POST['phone']
            date = datetime.datetime.now()
            total = total
            details = []
            for cart_product in cart_products:
                details.append(cart_product.book_name)
                details.append(cart_product.book_price)
            product_details = ','.join(details)
            message = ('Thanku For Your Order' +'\n' +'OrderId:' + order_id +'\n' + name + '\n'  + address +'\n'  + city +'\n'  + email +'\n'  + phone +'\n'  +  product_details )
            qr_code(message,order_id)
            img = f'qrcode/{order_id}.png'
            OrderPlaceDetails(user_id = user_id ,order_id =order_id ,order_details = product_details,date =date,qrcode =img,total =total).save()
            param_dict = {
                'MID': MERCHANT_ID,
                'ORDER_ID':str(order_id),
                'TXN_AMOUNT':str(total),
                'CUST_ID':email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'Cart/paytm.html', {'param_dict': param_dict ,'name':name})
        return render(request,'Cart/checkout.html',{'data':current_user,'cart_product':cart_products,'a':total})
    else:
        return redirect('login')


def compare_page(request):   # for a compareing a products..
    return render(request,'Cart/compare.html')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            orderid =response_dict['ORDERID']
            placeorderdetails = get_object_or_404(OrderPlaceDetails, order_id=orderid)
            user_id = placeorderdetails.user_id
            user = get_object_or_404(Register, user_id= user_id)
            TXNID =response_dict['TXNID']
            PAYMENTMODE =response_dict['PAYMENTMODE']
            STATUS =response_dict['STATUS']
            BANKTXNID =response_dict['BANKTXNID']
            placeorderdetails.TXNID =TXNID
            placeorderdetails.paymentmode =PAYMENTMODE
            placeorderdetails.status =STATUS
            placeorderdetails.BANKTXNID =BANKTXNID
            file = open(f'media/invoice/{TXNID}.txt', 'w')
            file.write("TXNID:" + TXNID)
            file.close()
            file = f'invoice/{TXNID}.txt'
            placeorderdetails.invoice = file
            placeorderdetails.save()
            placeorderdetails = get_object_or_404(OrderPlaceDetails, order_id=orderid)
            return render(request,'Cart/invoice.html',{'user':user,'orderdata':placeorderdetails})
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'Cart/invoice.html', {'response': response_dict})

