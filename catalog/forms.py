from django import forms


class TriangleForm(forms.Form):
    side_1 = forms.IntegerField(label='First side of triangle', required=True, min_value=1)
    side_2 = forms.IntegerField(label='Second side of triangle', required=True, min_value=1)
