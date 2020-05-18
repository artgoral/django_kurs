# coding: UTF-8
# python 2 only
#from __future__ import unicode_laterals, absolute_import
##############################

from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, TemplateView  # modul generic - zawiera widoki generyczne czyli podstawowe widoki obiektu
from django.views.generic import View # na tym postawimy strone glowna
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Author # trzeba to zawsze importowac jesli chce sie uzyc
from .models import Book

class MainPageTemplatView(TemplateView):
	template_name = 'index.html'


class MainPageView(View):  # wywolanie klasa
	def get(self, request, *args, **kwargs):  # wywolanie
		return HttpResponse('OK - klasa') 



index_view = MainPageView.as_view()

#def index_view(request, *args, **kwargs):  # wywolanie funkcja
	#return HttpResponse('OK - funkcja')


class AuthorListView(ListView):  # do pokazywania listy
	model = Author
	
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		super(AuthorListView, self).dispatch(*args, **kwargs)

class AuthorDetailView(DetailView): # do klikania i przenoszenia sie dalej
	model = Author

class BookListView(ListView):
	model = Book

class BookDetailView(DetailView):
	model = Book
