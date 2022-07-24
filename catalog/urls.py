from django.urls import path
from catalog.views import triangle

app_name = 'catalog'
urlpatterns = [
    path('', triangle, name='triangle'),

]
