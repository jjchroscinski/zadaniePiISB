
from django.contrib import admin
from django.urls import path
from bazaFilmowa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name='index'),
    # path('aktorzy/', views.aktorzy, name='aktorzy'),
    # path('rezyserzy/', views.rezyserzy, name='rezyserzy'),
    # path('filmy/', views.filmy, name='filmy'),
    # path('aktor/<int:id>/', views.aktor, name='aktor'),
    # path('dodajAktora/', views.dodajAktora, name='dodaj'),
    # path('usuwanieAktora/<int:id>/', views.usuwanieAktora, name='usuwanieAktora'),
    # path('aktualizacjaAktora/<int:id>/', views.aktualizacjaAktora, name='aktualizacjaAktora'),
    # path('', views.Index.as_view(), name='index'),
    # path('aktorzy/', views.AktorList.as_view(), name='aktorzy' ),
    # path('aktor/<slug:pk>/', views.AktorDetail.as_view(), name='aktor' ),
    # path('dodajAktora/', views.AktorCreate.as_view(), name='dodajAktora' )

]
