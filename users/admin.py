from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _ # zeby podkrezlniki  w fieldsetach sie nie wysypaly

from .models import BiblioUser


class BiblioUserAdmin(UserAdmin):
	fieldsets = ( # definiuje jak ma wygladac formularz edycyjny na stronie
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Additional info'), {'fields': ('avatar', 'phone')}),
    )

	
admin.site.register(BiblioUser, BiblioUserAdmin)
