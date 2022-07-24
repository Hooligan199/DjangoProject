from django.urls import path
from catalog.views import triangle


urlpatterns = [
    path('', triangle, name='triangle'),

]
