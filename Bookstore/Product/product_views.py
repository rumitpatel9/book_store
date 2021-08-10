from django.shortcuts import render,get_object_or_404
from .product_models import Books
from Authentication.authentication_models import Register
from Authentication import authentication_views
from .product_models  import *
from django.db.models import Q
from django.contrib import messages
from playsound import playsound
from gtts import gTTS

# Create your views here.

def convert_text_to_audio(book_name, bookid):
    book_audio =gTTS(book_name)
    book_audio.save(f'media/gtts/{bookid}.mp3')

def index(request):
    home_page_products = Books.objects.all()
    if request.method == 'POST':   # for a subscriber....
        email = request.POST['email']
        message = 'Now you are our subscriber.'
        authentication_views.sendemail(email, message)

    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register, user_id=request.session['user_id'])
        return render(request,'Product/index-18.html', {'NewArrival':home_page_products,'data':current_user})
    else:
        return render(request, 'Product/index-18.html', {'NewArrival': home_page_products})


def blog_details(request):
    blog_comments = BlogCommentPersonDetails.objects.all()
    if request.method == 'POST':   # if person add comment..
        name = request.POST['username']
        comment = request.POST['massage']
        img = request.FILES.get('img')
        BlogCommentPersonDetails(name=name,comment =comment,image =img).save()

    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register, user_id=request.session['user_id'])
        return render(request, 'Product/blog-details.html', {'data':current_user,'blogcomment': blog_comments})
    else:
        return render(request, 'Product/blog-details.html', {'blogcomment': blog_comments})


def blog(request):
    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register, user_id=request.session['user_id'])
        return render(request, 'Product/blog.html',{'data':current_user})
    else:
        return render(request, 'Product/blog.html')


def about(request):
    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register, user_id=request.session['user_id'])
        return render(request, 'Product/about.html',{'data':current_user})
    else:
        return render(request, 'Product/about.html')


def single_book(request, bookid):
    ###convert book details into audio..
    book_data = get_object_or_404(Books, pk=bookid)
    book_name = book_data.book_name
    try:
        convert_text_to_audio(book_name, bookid)
    except:
        pass
    ###play books details...
    if request.method == 'POST':
        playsound(f'media/gtts/{bookid}.mp3')

    if request.session.has_key('user_id'):
        profile = get_object_or_404(Register, user_id=request.session['user_id'])
        return render(request, 'Product/single.html', {'data': profile, 'bookdetails': book_data})
    else:
        return render(request, 'Product/single.html', {'bookdetails': book_data})



def books_page(request):
    All_Book = Books.objects.all()

    ###when user search somthing ......
    if request.method == 'POST':
        if request.POST.get('main') == 'main':
            global result
            result = request.POST.get('searchresult')
            find = Books.objects.filter(Q(book_publisher=result) | Q(book_author_name=result))
            return render(request, 'Product/shop.html', {'All_Book': All_Book,'find': find, 'find_data': 'FIND_DATA'})
        else:
            try:
                price = request.POST.get('sortdata')
                if price == 'high':
                    sort = Books.objects.filter(Q(book_publisher=result) | Q(book_author_name=result)).order_by('-book_offer_price')
                else:
                    sort = Books.objects.filter(Q(book_publisher=result) | Q(book_author_name=result)).order_by('book_offer_price')
                return render(request, 'Product/shop.html', {'All_Book': All_Book,'sort': sort, 'sort_data': 'SORT_DATA'})
            except:
                price = request.POST.get('sortdata')
                if price == 'high':
                    sort = Books.objects.filter().order_by('-book_offer_price')
                else:
                    sort = Books.objects.filter().order_by('book_offer_price')
                return render(request, 'Product/shop.html', {'All_Book': All_Book,'sort': sort, 'sort_data': 'SORT_DATA'})
    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register, user_id=request.session['user_id'])
        return render(request, 'Product/shop.html', {'data': current_user,'All_Book': All_Book})
    else:
        return render(request, 'Product/shop.html', {'All_Book': All_Book})


def romantic(request):
    All_Book = Books.objects.all()
    romantic_books = Books.objects.filter(books_data__categories_name='Romance')

    ###when user search somthing ......
    if request.method == 'POST':
        if request.POST.get('main') == 'main':
            global results
            results = request.POST.get('searchresult')
            find = Books.objects.filter((Q(book_publisher=results) | Q(book_author_name=results)) & Q(books_data__categories_name='Romance'))
            return render(request, 'Product/shop.html', {'find': find, 'find_data': 'FIND_DATA'})
        else:
            try:
                sort = request.POST.get('sortdata')
                if sort =='high':
                    sort = Books.objects.filter((Q(book_publisher=results) | Q(book_author_name=results)) &Q(books_data__categories_name='Romance')).order_by('-book_offer_price')
                else:
                    sort = Books.objects.filter((Q(book_publisher=results) | Q(book_author_name=results)) & Q(books_data__categories_name='Romance')).order_by('book_offer_price')
                return render(request, 'Product/shop.html', {'sort': sort,'sort_data': 'SORT_DATA'})
            except:
                sort = request.POST.get('sortdata')
                if sort == 'high':
                    sort = Books.objects.filter(Q(books_data__categories_name='Romance')).order_by('-book_offer_price')
                else:
                    sort = Books.objects.filter(Q(books_data__categories_name='Romance')).order_by('book_offer_price')
                return render(request, 'Product/shop.html', {'sort': sort, 'sort_data': 'SORT_DATA'})
    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register, user_id=request.session['user_id'])
        return render(request, 'Product/shop.html', {'data': current_user,'romance_books': romantic_books,'Romantic':'romantic','All_Book': All_Book})
    else:
        return render(request, 'Product/shop.html', {'romance_books': romantic_books, 'Romantic':'romantic','All_Book': All_Book})


def drama(request):
    All_Book = Books.objects.all()
    Drama_books = Books.objects.filter(books_data__categories_name='Drama')

    #  when user search somthing ......
    if request.method == 'POST':
        if request.POST.get('main') == 'main':
            global results
            results = request.POST.get('searchresult')
            find = Books.objects.filter((Q(book_publisher=results) | Q(book_author_name=results)) & Q(books_data__categories_name='Drama'))
            return render(request, 'Product/shop.html', {'find': find, 'find_data': 'FIND_DATA'})
        else:
            try:
                sort = request.POST.get('sortdata')
                if sort == 'high':
                    sort = Books.objects.filter((Q(book_publisher=results) | Q(book_author_name=results)) & Q(books_data__categories_name='Drama')).order_by('-book_offer_price')
                else:
                    sort = Books.objects.filter((Q(book_publisher=results) | Q(book_author_name=results)) & Q(books_data__categories_name='Drama')).order_by('Book_Offer_Price')
                return render(request, 'Product/shop.html', {'sort': sort, 'sort_data': 'SORT_DATA'})
            except:
                sort = request.POST.get('sortdata')
                if sort == 'high':
                    sort = Books.objects.filter(Q(books_data__categories_name='Drama')).order_by('-book_offer_price')
                else:
                    sort = Books.objects.filter(Q(books_data__categories_name='Drama')).order_by('book_offer_price')
                return render(request, 'Product/shop.html', {'sort': sort, 'sort_data': 'SORT_DATA'})
    if request.session.has_key('user_id'):
        current_user = get_object_or_404(Register, user_id=request.session['user_id'])
        return render(request, 'Product/shop.html',{'data': current_user, 'drama_books': Drama_books, 'Drama': 'drama', 'All_Book': All_Book})
    else:
        return render(request, 'Product/shop.html',{'drama_books': Drama_books,  'Drama': 'drama', 'All_Book': All_Book})


