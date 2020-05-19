# plik api.py wewnatrz aplikacji
# definicje widokow (ViewSet, View itd. )

from rest_framework import viewsets, permissions
from .models import Author
from .serializers import AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet): # zestaw pewnych widokow
	queryset = Autor.objects.all()
	serializer_class = AuthorSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  # sprawdza czy podano dane uwierzytelniajace
