# plik api_v1.py wewnatrz katalogu konfiguracyjnego projektu
# tutaj definiuje strukture mojego API

from rest_framework import routers

from shelf.api import AuthorViewSet # shelf/ api.py

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewSet)
