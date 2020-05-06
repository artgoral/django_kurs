from django.contrib import admin
from django.urls import path

from rental.views import RentalListView, RentalDetailView

app_name = 'rental'

urlpatterns = [
    
    path('rentallist/', RentalListView.as_view(), name='rental-list'),
    path('rentallist/(?P<pk>\d+/)', RentalDetailView.as_view(), name='rental-detail'),  #powiazanie miedzy wzorcem sciezki a widokiem
    
]
