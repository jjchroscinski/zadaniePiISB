from .models import Aktor, Rezyser, Film, Ocena
from rest_framework import viewsets
from .serializer import *

class AktorViewSet(viewsets.ModelViewSet):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer

class RezyserViewSet(viewsets.ModelViewSet):
    queryset = Rezyser.objects.all()
    serializer_class = RezyserSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class OcenaViewSet(viewsets.ModelViewSet):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer