from django.db import models

# Create your models here.


class BlogCommentPersonDetails(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='comment_person_name',blank=True)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class BooksCategories(models.Model):
    categories_name = models.CharField(max_length=200)

    def __str__(self):
        return self.categories_name


class Books(models.Model):
    books_data = models.ForeignKey(BooksCategories,on_delete=models.CASCADE, default=1)
    book_image = models.ImageField(upload_to='books')
    book_name = models.CharField(max_length=100)
    book_offer_price = models.FloatField(default=0)
    book_actual_price = models.FloatField(default=0)
    book_author_name = models.CharField(max_length=200,default='')
    book_publisher = models.CharField(max_length=200,default='')
    book_language = models.CharField(max_length=200,default='')
    book_total_pages = models.PositiveIntegerField(default=0)
    book_published_year = models.CharField(max_length=200,default='')
    book_details = models.TextField(default='')