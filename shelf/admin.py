# coding: UTF-8
# python 2 only
#from __future__ import unicode_laterals, absolute_import
##############################

from django.contrib import admin

from .models import Author, Publisher, Book, BookCategory, BookEdition, BookItem
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	search_fields = ['last_name', 'first_name']  #wyszukiwarka
	ordering = ['last_name', 'first_name']  # ustawianie kolejnosci

class BookAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ['title']  # dodaje liste kolum ktora wyswieta sie dodatkowo do tytulu

admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin) # podaje indywidualnie model oraz kalse administracyjna ktora ma nim zarzadzac

admin.site.register([Publisher, BookCategory, BookEdition, BookItem]) # podaje liste modeli ktore chcemy zarejestrowac
