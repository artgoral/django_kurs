from django import forms
from .models import Message

class MessageForm(forms.ModelForm):  # tworzenie formularza po modelu
	
	class Meta: # dajemy to w podklasie meta poniewaz pobieramy tylko info z modelu, wyzej mozemy dodawac wlasne zmienne dla tej klasy
		model = Message
		fields = ('name', 'email', 'message')  # musi byc to przepisane z models; dobrym nawykiem jest dodawac recznie uniknie sie prolemow

# to samo tylko bez wykorzystania modelu

class ContactForm(forms.Form):  # tworzenie formularza juz tylko w zakladce forms
	name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea())
	
	def clean_name(self):  # funkcja sprawdzajaca poprawnosc wypelnienia
		data = self.cleaned_data['name']  # cleaned_data - atrybut zawierajacy przygotowane dane
		if "D" not in data:
			raise forms.ValidationError("Twoje imie musi miec imei zawierajace 'D'!")
		return data
