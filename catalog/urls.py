from django.urls import path
from catalog.views import triangle, person, person_with_id

app_name = 'catalog'

urlpatterns = [
    path('triangle/', triangle, name='triangle'),
    path('person/', person, name='person'),
    path('person/<int:pk>', person_with_id, name='person_id'),
]
