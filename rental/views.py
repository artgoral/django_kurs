from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Rental

from django.views.generic import ListView, DetailView

from .models import Rental

class BookRentView(CreateView):
	model = Rental
	fields = ['who', 'what']
	success_url = '/' # sukces zapisywania

class RentalListView(ListView):  # do pokazywania listy
	model = Rental

class RentalDetailView(DetailView): # do klikania i przenoszenia sie dalej
	model = Rental
