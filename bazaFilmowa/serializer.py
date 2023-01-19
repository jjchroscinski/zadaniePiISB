from .models import Aktor, Rezyser, Film, Ocena
from django.contrib.auth.models import User
from rest_framework import serializers

class AktorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Aktor
        fields='__all__'

class RezyserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Rezyser
        fields='__all__'

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    iloscOcen=serializers.SerializerMethodField()
    srednia=serializers.SerializerMethodField()

    class Meta:
        model=Film
        fields='__all__'

    def get_iloscOcen(self, obj):
        a = Ocena.objects.filter(film=obj.id)

        return len(a)

    def get_srednia(self, obj):
        all_oceny = Ocena.objects.filter(film=obj.id).values('wartosc')
        oceny=[ocena['wartosc']for ocena in all_oceny]
        if len(all_oceny)>0:
            sr=round(sum(oceny)/len(all_oceny), 2)
        else:
            sr=f'Ten film jeszcze nie został oceniony'
        return sr



    def create(self, validated_data):

        return Film.objects.create(**validated_data)

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']

class OcenaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Ocena
        fields='__all__'