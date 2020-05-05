# coding: UTF-8
# python 2 only
#from __future__ import unicode_literals, absolute_import, print_function
#from django.utils.encoding import python_2_unicode_compatabile
#from six.moves import range   # biblioteka six pozwala na wspolprace python 2 i 3 - trzeba ja pobrac normalnie
##############################

from django.db import models
# from raport.models import Raport   -  importowanie jakiegos modelu z zewnatrz

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


class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author) # moze byc kilku autorow
	# author = models.ForeignKey('Author', on_delete=models.DO_NOTHING,)
	isbn =  models.CharField(max_length=17)
	publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING,)
	
	def __str__(self):
		return self.title

# raport = models.ForeignKey("raports.Raport")   - wczytywanie importowanego modelu
