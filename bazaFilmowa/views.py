from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):

    aktorzy= Aktor.objects.all()
    dane={'aktorzy' : aktorzy}
    return render(request,'szablon.html', dane)


def aktor(request, id):
    aktor_user=Aktor.objects.get(pk=id)
    return HttpResponse(aktor_user)

