"""biblio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from django.urls import include

from shelf.views import AuthorListView, AuthorDetailView # dodajemy to oczywiscie/ to nie musi byc jezeli robimy zewnetrzny urls
from shelf.views import BookListView, BookDetailView											# dla drugiego sposobu wywalam te importy do odpowiednich urls
from contact.views import MessageAddView
from rental.views import RentalListView, RentalDetailView
from shelf.views import MainPageView, MainPageTemplatView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('shelf/', include('shelf.shelfurls', namespace='shelf')),
    # path('authors/', AuthorListView.as_view(), name='author-list'),
    # dla drugiej metody path('authors/', 'shelf.urls'),  # wtedy wszystkie linki dla authors sa pobierane z innego pliku
    # path('authors/(?P<pk>\d+/)', AuthorDetailView.as_view(), name='author-detail'),  #powiazanie miedzy wzorcem sciezki a widokiem
    path('contact/', MessageAddView.as_view()),
    path('rental/', include('rental.rentalurls', namespace='rental')),
    path('', MainPageView.as_view(), name='main-page'), # puste miejsce w cudzyslowie zeby bylo glowna strona
    #path('', 'shelf.views.index_view', name='main-page'),  # do odpalnia glownej strony z funkcji
    path('mainpagetemplate/', MainPageTemplatView.as_view(), name='mainpage-template'),
]
