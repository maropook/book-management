# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    filter_fields = ('book_id', 'title', 'title_kana',
                     'author', 'author_kana', 'isbn', 'sales_date')
    search_fields = ('book_id', 'title', 'title_kana',
                     'author', 'author_kana', 'isbn', 'sales_date')
