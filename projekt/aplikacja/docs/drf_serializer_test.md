## Przykład wykorzystania serializerów OsobaSerializer i StanowiskoSerializer

```python
from aplikacja.models import Osoba, Stanowisko
from aplikacja.serializers import OsobaSerializer, StanowiskoSerializer

# Tworzenie przykładowych obiektów
stanowisko = Stanowisko(nazwa='Programista', opis='Zajmuje się tworzeniem oprogramowania')
stanowisko.save()

osoba = Osoba(imie='Jan', nazwisko='Kowalski', plec=1, wiek=30, data_urodzenia='1993-01-01', stanowisko=stanowisko)
osoba.save()

# Serializacja obiektu Osoba
osoba_serializer = OsobaSerializer(osoba)
print(osoba_serializer.data)

# Serializacja obiektu Stanowisko
stanowisko_serializer = StanowiskoSerializer(stanowisko)
print(stanowisko_serializer.data)

# Deserializacja danych do obiektu Osoba
osoba_data = {
    'imie': 'Anna',
    'nazwisko': 'Nowak',
    'plec': 2,
    'wiek': 25,
    'data_urodzenia': '1998-05-15',
    'stanowisko': stanowisko.id
}
osoba_serializer = OsobaSerializer(data=osoba_data)
if osoba_serializer.is_valid():
    nowa_osoba = osoba_serializer.save()
    print(nowa_osoba)
else:
    print(osoba_serializer.errors)
```