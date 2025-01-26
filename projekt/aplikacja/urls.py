from django.urls import path
from .views import OsobaList, OsobaDetail, OsobaSearch, StanowiskoList, StanowiskoDetail, PersonUpdateView, PersonDeleteView

urlpatterns = [
    # Endpointy dla modelu Osoba
    path('osoby/', OsobaList.as_view(), name='osoba-list'),
    path('osoby/<int:pk>/', OsobaDetail.as_view(), name='osoba-detail'),
    path('osoby/search/', OsobaSearch.as_view(), name='osoba-search'),

    # Endpointy dla modelu Stanowisko
    path('stanowiska/', StanowiskoList.as_view(), name='stanowisko-list'),
    path('stanowiska/<int:pk>/', StanowiskoDetail.as_view(), name='stanowisko-detail'),

    # Endpointy dla modelu Person
    path('person/<int:pk>/update/', PersonUpdateView.as_view(), name='person-update'),
    path('person/<int:pk>/delete/', PersonDeleteView.as_view(), name='person-delete'),
]