# Generated by Django 4.1.3 on 2022-12-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaFilmowa', '0002_alter_film_premiera_alter_ocena_wartosc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aktor',
            options={'verbose_name': 'Aktor', 'verbose_name_plural': 'Aktorzy'},
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'verbose_name': 'Film', 'verbose_name_plural': 'Filmy'},
        ),
        migrations.AlterModelOptions(
            name='ocena',
            options={'verbose_name': 'Ocena', 'verbose_name_plural': 'Oceny'},
        ),
        migrations.AlterModelOptions(
            name='rezyser',
            options={'verbose_name': 'Reżyser', 'verbose_name_plural': 'Reżyserzy'},
        ),
        migrations.AddField(
            model_name='film',
            name='aktorzy',
            field=models.ManyToManyField(to='bazaFilmowa.aktor'),
        ),
    ]