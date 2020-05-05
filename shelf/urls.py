from django.contrib import admin
from django.urls import path

from shelf.views import AuthorListView, AuthorDetailView # dodajemy to oczywiscie


urlpatterns = [
    
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/(?P<pk>\d+/)', AuthorDetailView.as_view(), name='author-detail'),  #powiazanie miedzy wzorcem sciezki a widokiem
    
]
