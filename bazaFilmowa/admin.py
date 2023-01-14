from django.contrib import admin
from .models import Aktor, Rezyser, Film, Ocena

# Register your models here.

class OcenyFilmu(admin.StackedInline):
    model = Ocena
@admin.register(Aktor)
class AktorAdmin(admin.ModelAdmin):
    list_display = [
        'nazwisko',
        'imie'
    ]
    search_fields = ['nazwisko']
    def __str__(self):
        return f'ID: {self.id}'

@admin.register(Rezyser)
class RezyserAdmin(admin.ModelAdmin):
    list_display = [
        'nazwisko',
        'imie'
    ]
    search_fields = ['nazwisko']
    def __str__(self):
        return f'ID: {self.id}'

@admin.register(Ocena)
class OcenaAdmin(admin.ModelAdmin):
    list_display = [
        'film',
        'wartosc'
    ]
    search_fields = ['film']
    def __str__(self):
        return f'ID: {self.id}'

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = [
        'id' ,
        'nazwa',
        'created',
    ]
    search_fields = ['nazwa']
    inlines=[
        OcenyFilmu
    ]


    def __str__(self):
        return f'ID: {self.id}'