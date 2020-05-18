
from django import forms
from .modules import Rental

class BookRentForm(forms.modelForm):
	class Meta:
		model = Rental
		fields = ['who', 'what']
