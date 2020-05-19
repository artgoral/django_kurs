from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import Permission  # sposob 1

from django.db.models.signals import pre_save, post_save # sposb 2
from django.dispatch import receiver  # sposb 2

import logging # sposob 1
logger = logging.getLogger('django') # sposob 1
							# moge nazwac jakkolwiek chce - sluzy to do obslugi loggerow
class BiblioUser(AbstractUser):
	avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, default='')
	
	class Meta:
		permissions = (
			('can_rent', 'Can rent a book'),
		)

	def save(self, *args, **kwargs):
		# sposob 1
		super(BiblioUser, self).save(*args, **kwargs)
		try:
			p = Permission.objects.get(codename='can_rent')
			self.user_permissions.add(p)
		except Exception as e: # Permission.DoesNoExist
			# logowanie bledu
			logger.log(logging.ERROR, "%s" % e)

		
		
# sposob 2 - sygnaly 
@receiver(post_save, sender=BiblioUser)
def add_rent_permission(sender, *args, **kwargs):
	user = kwargs.get('instance')
	try:
		p = Permission.objects.get(codename='can_rent')
		user.user_permissions.add(p)
		logger.info("Dodano pomyslnie uprawnienie.")
	except Exception as e: # Permission.DoesNoExist
		# logowanie bledu
		logger.error("Wystapil blad w nadawaniu uprawnienia: %s" % e)

