## 1. Wyświetl wszystkie obiekty modelu Osoba
```python
from aplikacja.models import Osoba, Stanowisko
osoby = Osoba.objects.all()
print(osoby)
```

## 2. Wyświetl obiekt modelu Osoba z id = 3
```python
osoba_id_3 = Osoba.objects.get(id=3)
print(osoba_id_3)
```

## 3. Wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na literę 'A'
```python
osoby_na_a = Osoba.objects.filter(imie__startswith='A')
print(osoby_na_a)
```

## 4. Wyświetl unikalną listę stanowisk przypisanych dla modeli Osoba
```python
unikalne_stanowiska = Stanowisko.objects.filter(osoba__isnull=False).distinct()
print(unikalne_stanowiska)
```

## 5. Wyświetl nazwy stanowisk posortowane alfabetycznie malejąco
```python
stanowiska_malejaco = Stanowisko.objects.order_by('-nazwa')
print(stanowiska_malejaco)
```

## 6. Dodaj nową instancję obiektu klasy Osoba i zapisz w bazie
```python
nowa_osoba = Osoba(imie='Jan', nazwisko='Kowalski', plec=1, wiek=30, data_urodzenia='1993-01-01', stanowisko_id=1)
nowa_osoba.save()
print(nowa_osoba)
```