from django.db import models

# Create your models here.
from django.db import models


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    title_kana = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    author_kana = models.CharField(max_length=250)
    isbn = models.CharField(max_length=250)
    sales_date = models.CharField(max_length=250)
