from django.http import HttpResponse
from django.shortcuts import render
from .models import Aktor, Film, Rezyser, Ocena
import datetime


def index(request):

    filmy = Film.objects.all()
    aktor = Aktor.objects.all()
    dane={
        'filmy' : filmy,
        'aktor' : aktor
    }
    return render(request, 'bazaFilmowa/index.html', dane)


def aktorzy(request):
    aktorzy=Aktor.objects.all()
    dane = {'aktorzy': aktorzy}
    return render(request,'bazaFilmowa/aktorzy.html', dane)
def aktor(request, id):
    aktor_user=Aktor.objects.get(pk=id)
    aktorzy = Aktor.objects.all()
    dane = {
        'aktor': aktor_user,
        'aktorzy': aktorzy
    }
    return render(request,'bazaFilmowa/aktor.html', dane)

def rezyserzy(request):
    rezyserzy=Rezyser.objects.all()
    dane = {'rezyserzy': rezyserzy}
    return render(request,'bazaFilmowa/rezyserzy.html', dane)

def filmy(request):
    filmy = Film.objects.all()
    aktor = Aktor.objects.all()
    dane = {
        'filmy': filmy,
        'aktor': aktor
    }
    return render(request,'bazaFilmowa/filmy.html', dane)

