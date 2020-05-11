from django.db import models
#from django.contrib.auth.models import User  # who = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
from shelf.models import BookItem

from django.conf import settings

# Create your models here.

from django.utils.timezone import now  # funkcja do przypisywania daty stworzenia wraz z strefa czasowa


class Rental(models.Model):
	who = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,)
	what = models.ForeignKey(BookItem, on_delete=models.DO_NOTHING,)
	# when = models.DateTimeField(auto_now_add=True)  # auto_now_add=True - przy tworzeniu modelu dodaje date stworzenia ale bedzie wylaczone z mozliwosci edycji
	when = models.DateTimeField(default=now)  # default przypisuje coś domyślnego
	returned = models.DateTimeField(null=True, blank=True)  # (puste pole jest akceptowalne, dla front endu mowi o tym ze moze zostac puste pole)
	# nie wpisujemu null = True w pola typu CharField
	
	def __str__(self):
		return "Uzytkownik {who} wupozyczyl {what.catalogue_number} data {when}".format(who=self.who,  what=self.what, when=self.when)
