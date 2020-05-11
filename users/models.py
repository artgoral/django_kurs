from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class BiblioUser(AbstractUser):
	#avatar = models.ImageField(upload_to='avatars/')
	phone = models.CharField(max_length=15)

