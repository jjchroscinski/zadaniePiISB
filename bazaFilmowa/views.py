# from django.http import HttpResponseRedirect
# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.views.generic import ListView, DetailView, CreateView
# from .models import Aktor, Film, Rezyser, Ocena
# from .forms import AktorForm
#
# # #class view
# # class AktorList(ListView):
# #     model= Aktor
# #     template_name ='bazaFilmowa/aktor/aktorzy.html'
# #     context_object_name = 'aktor'
# #
# # class AktorDetail(DetailView):
# #     model = Aktor
# #     template_name = 'bazaFilmowa/aktor/aktor.html'
# #
# #  class AktorCreate(CreateView):
# #     model = Aktor
# #     form_class = AktorForm
# #     template_name ='bazaFilmowa/aktor/dodajAktora.html'
# #
# #
# #
# # class Index(ListView):
# #     model =Aktor
# #        # Film
# #
# #     template_name ='bazaFilmowa/index.html'
#
# #function view
# def index(request):
#
#     filmy = Film.objects.all()
#     aktor = Aktor.objects.all()
#     dane={
#         'filmy' : filmy,
#         'aktor' : aktor
#     }
#     return render(request, 'bazaFilmowa/index.html', dane)
#
#
# def aktorzy(request):
#     aktorzy=Aktor.objects.all()
#     dane = {'aktorzy': aktorzy}
#     return render(request,'bazaFilmowa/aktor/aktorzy.html', dane)
# def aktor(request, id):
#     aktor_user=Aktor.objects.get(pk=id)
#     aktorzy = Aktor.objects.all()
#     dane = {
#         'aktor': aktor_user,
#         'aktorzy': aktorzy
#     }
#     return render(request,'bazaFilmowa/aktor/aktor.html', dane)
#
# def rezyserzy(request):
#     rezyserzy=Rezyser.objects.all()
#     dane = {'rezyserzy': rezyserzy}
#     return render(request,'bazaFilmowa/rezyserzy.html', dane)
#
# def filmy(request):
#     filmy = Film.objects.all()
#     aktor = Aktor.objects.all()
#     dane = {
#         'filmy': filmy,
#         'aktor': aktor
#     }
#     return render(request,'bazaFilmowa/filmy.html', dane)
#
# def dodajAktora(request):
#     form = AktorForm(request.POST or None, request.FILES or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('aktorzy'))
#
#     dane={
#         "form" : form
#     }
#     return render(request,'bazaFilmowa/aktor/dodajAktora.html', dane)
#
# def aktualizacjaAktora(request, id):
#     aktor = Aktor.objects.get(pk=id)
#     form = AktorForm(request.POST or None, request.FILES or None, instance=aktor)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('aktorzy'))
#
#     dane={
#         "form" : form
#     }
#     return render(request,'bazaFilmowa/aktor/dodajAktora.html', dane)
#
# def usuwanieAktora(request, id):
#     aktor = Aktor.objects.get(pk=id)
#     aktor.delete()
#     return redirect(reverse('aktorzy'))