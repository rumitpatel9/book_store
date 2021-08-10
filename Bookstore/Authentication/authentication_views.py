from django.shortcuts import render,redirect,get_object_or_404
from .authentication_models import *
from django.contrib import messages
from Cart.cart_models import OrderPlaceDetails
import random
import smtplib

# Create your views here.

#send email to user.
def sendemail(TO,MESSAGE):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('bansupatel008@gmail.com', 'shruti123@')
    server.sendmail('bansupatel008@gmail.com', TO, MESSAGE)
    server.quit()

# create username
def create_userid():
    num_range = '0123456789'
    user_id = ''.join(random.sample(num_range, 10))
    return user_id


def login_page(request):
    if request.method == 'POST':
        try:
            user = Register.objects.get(user_id =request.POST.get('email'))
            if user.password == request.POST.get('password'):
                request.session['user_id'] = request.POST.get('email')  # user session created...
                return redirect('home')
            else:
                messages.info(request, 'Password wrong')
        except:
            messages.info(request, 'userid  wrong')
    return render(request, 'Authentication/login.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first name')
        last_name = request.POST.get('last name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        address = request.POST.get('address1') + request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        profile_img = request.FILES.get('img')
        password = request.POST.get('password')
        conform_password = request.POST.get('confirm password')
        if password == conform_password:
            if Register.objects.filter(email=email).exists():
                messages.info(request,'Email already exist')
            else:
                userid = create_userid()
                message = (first_name + 'your generated userid is ' + userid)
                try:
                    sendemail(email, message)
                except:
                    return redirect('error')
                Register(first_name=first_name, last_name=last_name, email=email, mobile_nu=phone, country=country,
                         address=address, city=city, state=state, pincode=pincode, password=password, user_id =userid, profile_image=profile_img).save()
                return redirect('login')
        else:
            messages.info(request, 'Password not match')
    return render(request, 'Authentication/register.html')


def logout_page(request):
    if request.session.has_key('user_id'):
        del request.session['user_id']
        return redirect('login')


def my_account_page(request):
    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register,user_id=request.session['user_id'])
        try:
            temp =0
            Oreder_data =OrderPlaceDetails.objects.filter(user_id=request.session['user_id'])
        except:
            temp =1
        # change my account profile..
        if request.method == 'POST':
            first_name = request.POST.get('first name')
            last_name = request.POST.get('last name')
            profile_image = request.FILES.get('img')
            email = request.POST.get('email')
            current_password = request.POST.get('current password')
            current_user.First_Name = first_name
            current_user.Last_Name = last_name
            current_user.Profile_Image = profile_image
            current_user.Email = email
            current_user.Password = current_password
            current_user.save()
            return render(request, 'Authentication/my-account.html', {'data': current_user})
        if temp == 1:
            return render(request, 'Authentication/my-account.html',{'data': current_user})
        else:
            return render(request, 'Authentication/my-account.html', {'data': current_user, 'Oreder_data': Oreder_data})
    else:
        return redirect('login')


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact(Name=name, Email=email, Subject=subject, Message=message).save()
        message = ('Hello' + name + ' Thankyou for the visited our store.our team will contect  you shortly.')
        try:
            sendemail(email, message)
        except:
            return redirect('error')
        return redirect('home')
    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register, user_id=request.session['user_id'])
        return render(request, 'Authentication/contact.html', {'data':current_user})
    else:
        return render(request, 'Authentication/contact.html')


def error_404_page(request):
    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register, user_id=request.session['user_id'])
        return render(request, 'Authentication/404.html', {'data': current_user})
    else:
        return render(request, 'Authentication/404.html')


