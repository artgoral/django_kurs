# coding: UTF-8
# python 2 only
#from __future__ import unicode_laterals, absolute_import
##############################

from django.contrib import admin

from .models import Author, Publisher, Book
# Register your models here.

admin.site.register([Author, Publisher, Book])
