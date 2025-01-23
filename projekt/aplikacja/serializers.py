from rest_framework import serializers
from .models import Team, Person, Osoba, Stanowisko

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model: Team
        fields: '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model: Person
        fields: '__all__'

class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model: Osoba
        fields: '__all__'

class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model: Stanowisko
        fields: '__all__'
