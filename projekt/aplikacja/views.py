from django.shortcuts import render
from rest_framework import generics
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer

# Widoki dla modelu Osoba
class OsobaList(generics.ListCreateAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer

class OsobaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer

class OsobaSearch(generics.ListAPIView):
    serializer_class = OsobaSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query:
            return Osoba.objects.filter(nazwisko__icontains=query)
        return Osoba.objects.all()

# Widoki dla modelu Stanowisko
class StanowiskoList(generics.ListCreateAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer

class StanowiskoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer