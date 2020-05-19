from django.shortcuts import render

# Create your views here.
# FormView jest to widok pozwalajacy na przetworzenie formularza
from django.views.generic import ListView, DetailView, FormView
from .models import Message
from .forms import MessageForm, ContactForm

class MessaDetailView(DetailView):  
	model = Message

class MessageAddView(FormView): 
	form_class = ContactForm  # MessageForm - jezeli wybiore to to odpali sie drugi sposob
	template_name = 'contact/message_form.html'
	success_url = '/'
	
	def form_valid(self, form):  # jest uruchamiana wtedy gdy formularz zostanie uznany za poprawny
		form.save()  # bo form jest instancja ModelForm, ktory posiada metoda save()
		return super(MessageAddView, self).form_valid(form)  # odwolujemy sie do klasy pierwotnej
