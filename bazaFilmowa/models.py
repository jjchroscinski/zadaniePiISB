from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Aktor(models.Model):
    imie=models.CharField(max_length=45)
    nazwisko=models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = u'Aktorzy'

    def __str__(self):
        return self.imie+' '+self.nazwisko

class Rezyser(models.Model):
    imie=models.CharField(max_length=45)
    nazwisko=models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = u'Reżyserzy'

    def __str__(self):
        return self.imie+' '+self.nazwisko


class Film(models.Model):
    nazwa=models.CharField(max_length=45)
    opis = models.TextField(max_length=255)
    slug=models.SlugField(max_length=45, blank=True, null=True)
    created=models.DateTimeField(auto_now_add = True)
    updated=models.DateTimeField(auto_now = True)
    rezyser=models.ManyToManyField(Rezyser)
    aktorzy=models.ManyToManyField(Aktor)

    class Meta:
        verbose_name_plural = u'Filmy'

    def __str__(self):
        return self.nazwa



class Ocena(models.Model):
    class OCENY(models.IntegerChoices):
        tragiczn=1
        ujdzie=2
        sredni=3
        dobry=4
        swietny=5

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    wartosc=models.IntegerField(choices=OCENY.choices)

    class Meta:
        verbose_name_plural = u'Oceny'
        unique_together=[['user', 'film']]

    def __str__(self):
        return f'ID: {self.id}'