# coding: UTF-8
# python 2 only
#from __future__ import unicode_laterals, absolute_import
##############################

from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView  # modul generic - zawiera widoki generyczne czyli podstawowe widoki obiektu

from .models import Author # trzeba to zawsze importowac jesli chce sie uzyc
from .models import Book

class AuthorListView(ListView):  # do pokazywania listy
	model = Author

class AuthorDetailView(DetailView): # do klikania i przenoszenia sie dalej
	model = Author

class BookListView(ListView):
	model = Book
