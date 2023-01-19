from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import filters

from .serializer import *

class AktorViewSet(viewsets.ModelViewSet):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['imie', 'nazwisko']

    def get_permissions(self):

        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class RezyserViewSet(viewsets.ModelViewSet):
    queryset = Rezyser.objects.all()
    serializer_class = RezyserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['imie', 'nazwisko']
    def get_permissions(self):

        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['nazwa', 'slug']
    ordering = ['iloscOcen']
    def get_permissions(self):

        if self.action=='list' or self.action=='retrieve':
            permission_classes=[AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class OcenaViewSet(viewsets.ModelViewSet):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer

    def get_permissions(self):

        if self.action=='list':
            permission_classes=[AllowAny]
        elif self.action=='create' """orself.action=='create'""":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):

        if self.action=='create':
            permission_classes=[AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]