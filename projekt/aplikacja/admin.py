from django.contrib import admin
from .models import Team, Person, Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ('data_dodania',)
    list_display = ('imie', 'nazwisko', 'stanowisko', 'data_dodania')

    @admin.display(description='Stanowsiko')
    def stanowisko_display(self, obj):
        return f"{obj.stanowisko.nazwa} ({obj.stanowisko.opis})"

class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'opis')
    list_filter = ('nazwa',)

admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)
