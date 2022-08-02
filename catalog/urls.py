from django.urls import path
from catalog.views import triangle, person, person_with_id, catalog_main

app_name = 'catalog'

urlpatterns = [
    path('', catalog_main, name='catalog_name'),
    path('triangle/', triangle, name='triangle'),
    path('person/', person, name='person'),
    path('person/<int:pk>', person_with_id, name='person_id'),
]
