from django.contrib import admin
from django.urls import path

from shelf.views import AuthorListView, AuthorDetailView # dodajemy to oczywiscie

app_name = 'shelf'

urlpatterns = [
    
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/(?P<pk>\d+/)', AuthorDetailView.as_view(), name='author-detail'),  #powiazanie miedzy wzorcem sciezki a widokiem
    
]
