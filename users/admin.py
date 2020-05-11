from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import BiblioUser


class BiblioUserAdmin(UserAdmin):
	pass
	
admin.site.register(BiblioUser, BiblioUserAdmin)
