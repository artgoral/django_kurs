from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView

from .models import Rental

class RentalListView(ListView):  # do pokazywania listy
	model = Rental

class RentalDetailView(DetailView): # do klikania i przenoszenia sie dalej
	model = Rental
