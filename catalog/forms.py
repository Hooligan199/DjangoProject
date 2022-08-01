from django import forms
from django.forms import ModelForm
from .models import Person


class TriangleForm(forms.Form):
    side_1 = forms.IntegerField(label='First side of triangle', required=True, min_value=1)
    side_2 = forms.IntegerField(label='Second side of triangle', required=True, min_value=1)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
