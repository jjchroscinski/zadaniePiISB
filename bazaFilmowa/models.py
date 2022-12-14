from django.db import models

class Aktor(models.Model):
    imie=models.CharField(max_length=45)
    nazwsiko=models.CharField(max_length=45)

    class Meta:
        verbose_name = u'Aktor'
        verbose_name_plural = u'Aktorzy'

    def __str__(self):
        return self.imie+' '+self.nazwsiko

class Rezyser(models.Model):
    imie=models.CharField(max_length=45)
    nazwsiko=models.CharField(max_length=45)

    class Meta:
        verbose_name = u'Reżyser'
        verbose_name_plural = u'Reżyserzy'

    def __str__(self):
        return self.imie+' '+self.nazwsiko


class Film(models.Model):
    nazwa=models.CharField(max_length=45)
    opis = models.TextField()
    slug=models.SlugField(max_length=45, default='film')
    premiera=models.DateField('premiera')
    rezyser=models.ForeignKey(Rezyser, on_delete=models.CASCADE)
    aktorzy=models.ManyToManyField(Aktor)

    class Meta:
        verbose_name = u'Film'
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

    user = models.TextField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    wartosc=models.IntegerField(choices=OCENY.choices)
    created_data=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'Ocena'
        verbose_name_plural = u'Oceny'