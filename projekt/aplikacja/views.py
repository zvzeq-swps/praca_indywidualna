from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Osoba, Stanowisko, Person
from .serializers import OsobaSerializer, StanowiskoSerializer, PersonSerializer
from django.views import View
class ProfileView(View):
    template_name = 'profile.html'

    def get(self, request, username):
        user = User.objects.get(username=username)
        return render(request, self.template_name, {'user': user})

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

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.wlasciciel == request.user

# Widoki dla modelu Stanowisko
class StanowiskoList(generics.ListCreateAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer

class StanowiskoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer

# Widoki dla modelu Person
class PersonUpdateView(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDeleteView(generics.DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]