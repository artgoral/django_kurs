# plik serializers.py klasy przeksztalcajace obiekty z bazy do frameworku

from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		moedel = Author
		fields = ('first_name', 'last_name')



