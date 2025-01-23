from django.contrib import admin
from .models import Team, Person, Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ('data_dodania',)

admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko)
