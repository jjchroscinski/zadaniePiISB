from django.contrib import admin
from django.utils.html import format_html
from .models import Aktor, Rezyser, Film, Ocena

# Register your models here.

@admin.register(Aktor)
class AktorAdmin(admin.ModelAdmin):
    list_display = ['nazwsiko', 'imie' ]

    def __str__(self):
        return f'ID: {self.id}'

@admin.register(Rezyser)
class RezyserAdmin(admin.ModelAdmin):
    list_display = ['nazwsiko', 'imie' ]

    def __str__(self):
        return f'ID: {self.id}'

@admin.register(Ocena)
class OcenaAdmin(admin.ModelAdmin):
    list_display = ['film', 'wartosc']

    def __str__(self):
        return f'ID: {self.id}'

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'rezyser','premiera']

    def __str__(self):
        return f'ID: {self.id}'