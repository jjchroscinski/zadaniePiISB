
from django.contrib import admin
from django.urls import path
from bazaFilmowa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('aktorzy/', views.aktorzy, name='aktorzy'),
    path('rezyserzy/', views.rezyserzy, name='rezyserzy'),
    path('filmy/', views.filmy, name='filmy'),
    path('aktor/<id>/', views.aktor, name='aktor'),
]
