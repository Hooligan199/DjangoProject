from math import sqrt
from django.shortcuts import render
from catalog.forms import TriangleForm


def triangle(request):
    if request.method == 'POST':
        triangle_form = TriangleForm(request.POST)
        if triangle_form.is_valid():
            data = triangle_form.cleaned_data
            answer = sqrt(data['side_1'] ** 2 + data['side_2'] ** 2)
            return render(request, 'catalog/geometry.html', {
                'triangle_form': TriangleForm(),
                'answer': answer.__round__(2),
            })
    else:
        triangle_form = TriangleForm()  # q1?
    return render(request, 'catalog/geometry.html', {
        'triangle_form': triangle_form,  # q1?
    })
