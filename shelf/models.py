# coding: UTF-8
# python 2 only
#from __future__ import unicode_literals, absolute_import, print_function
#from django.utils.encoding import python_2_unicode_compatabile
#from six.moves import range   # biblioteka six pozwala na wspolprace python 2 i 3 - trzeba ja pobrac normalnie
##############################

from django.db import models
from django.db.models import Model
# from raport.models import Raport   -  importowanie jakiegos modelu z zewnatrz

from django.urls import reverse_lazy, reverse # w tym przykladzie uzywamy tego w modelu Book
from datetime import datetime, date
from django.utils.timezone import now
from datetime import date

# @python_2_unicode_compatabile - trzeba dac ten dekorator wszedzie gdzie mamy funkcje str!!!!!!! - python 2
class Author(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=50)
	
	def __str__(self):
		return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)


class Publisher(models.Model):
	name = models.CharField(max_length=70)
	
	def __str__(self):
		return self.name


class BookCategory(models.Model):
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name

class Book(models.Model):
	"""
	Cos w rodzaju rekopisu
	"""
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author) # moze byc kilku autorow
	categories = models.ManyToManyField(BookCategory)
	# author = models.ForeignKey('Author', on_delete=models.DO_NOTHING,)
	
	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse_lazy('shelf:book-detail', kwargs={'pk':self.id})  # reverse_lazy zamienia nazwe widoku na konkretna sciezke

	
class BookEdition(Model):	
	"""
	Wydanie okreslonej ksiazki
	"""
	book = models.ForeignKey(Book,  on_delete=models.DO_NOTHING,)
	isbn = models.CharField(max_length=17, blank=True)
	date = models.DateField(null=True, blank=True)
	publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING,)
		
	def __str__(self):
		return "{book.title}, {publisher.name}, {isbn}, {date}".format(book=self.book, publisher=self.publisher, isbn=self.isbn, date=self.date)


COVER_TYPES = (
	('soft', 'Soft'),
	('hard', 'Hard'),
	# (wartosc_w_bazie, wartosc_wyswietlana)
	
)
	
class BookItem(models.Model):
	"""
	Okreslony egzemplarz
	"""
	edition = models.ForeignKey(BookEdition,  on_delete=models.DO_NOTHING,)
	catalogue_number = models.CharField(max_length=30)
	cover_type = models.CharField(max_length=4, choices = COVER_TYPES)
	
	def __str__(self):
		return "{edition}, {cover}".format(edition=self.edition, cover=self.get_cover_type_display()) # odpala wybieranie z opcji


# raport = models.ForeignKey("raports.Raport")   - wczytywanie importowanego modelu
