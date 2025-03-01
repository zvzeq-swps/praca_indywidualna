from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
import re
# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Grupy"

class Person(models.Model):
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Rozmiary koszulek"

class Plec(models.IntegerChoices):
    KOBIETA = 1, 'Kobieta'
    MEZCZYZNA = 2, 'Mężczyzna'
    INNE = 3, 'Inne'

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=60)
    opis = models.TextField()

    def __str__(self):
        return self.nazwa
    class Meta:
        verbose_name_plural = "Stanowiska"

class Osoba(models.Model):
    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=60)
    plec = models.IntegerField(choices=Plec.choices)
    wiek = models.IntegerField()
    data_urodzenia = models.DateField()
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateTimeField(auto_now_add=True)
    wlasciciel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='osoby')

    class Meta:
        verbose_name_plural = "Osoby"
        ordering = ['nazwisko', 'imie']

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
    
    def clean(self):
        if not re.match(r"^[A-Z][a-z]+$", self.imie, self.nazwisko):
            raise ValidationError("Imię i nazwisko muszą zaczynać się z wielkiej litery.")
        if self.wiek < 0:
            raise ValidationError("Wiek nie może być ujemny.")
        if self.data_urodzenia > datetime.date.today():
            raise ValidationError("Data urodzenia nie może być z przyszłości.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
