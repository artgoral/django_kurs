from django.contrib import admin
from django.urls import path
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators impor login_required

from shelf.views import AuthorListView, AuthorDetailView # dodajemy to oczywiscie
from shelf.views import BookListView, BookDetailView
from rental.views import BookRentView

app_name = 'shelf'

urlpatterns = [
    
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/(?P<pk>\d+/)', AuthorDetailView.as_view(), name='author-detail'),  #powiazanie miedzy wzorcem sciezki a widokiem
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/(?P<pk>\d+/)', BookDetailView.as_view(), name='book-detail'),
    path('books/(?P<pk>\d+/)/rent', BookRentView.as_view(), name='book-rent'),
]
