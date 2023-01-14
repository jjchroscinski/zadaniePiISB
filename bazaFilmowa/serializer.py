from .models import Aktor, Rezyser, Film, Ocena
from django.contrib.auth.models import User
from rest_framework import serializers

class AktorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Aktor
        fields=[
            'imie',
            'nazwisko'
        ]

    def create(self, validated_data):

        return Snippet.objects.create(**validated_data)

class RezyserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Rezyser
        fields=[
            'imie',
            'nazwisko'
        ]

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    iloscOcen=serializers.SerializerMethodField()
    srednia=serializers.SerializerMethodField()

    class Meta:
        model=Film
        fields=[
            'nazwa',
            'opis',
            'slug',
            'created',
            'updated',
            'rezyser',
            'aktorzy',
            'srednia',
            'iloscOcen'
        ]
        ordering = ['iloscOcen']
    def get_iloscOcen(self, obj):
        a = Ocena.objects.filter(film=obj.id)

        return len(a)

    def get_srednia(self, obj):
        a = Ocena.objects.filter(film=obj.id)
        suma=0
       # for i in  range(len(a)):
        #    suma=suma+a[i]['wartosc']

        return f'Tu powinna byc srednia'

    def create(self, validated_data):

        return Film.objects.create(**validated_data)

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']

class OcenaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Ocena
        fields=[
            'user',
            'film',
            'wartosc'
        ]