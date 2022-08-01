from math import sqrt
from django.shortcuts import render, get_object_or_404
from catalog.forms import TriangleForm, PersonForm
from .models import Person


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


def person(request):
    if request.method == 'POST':
        person_form = PersonForm()

        print('OK')
    else:
        person_form = PersonForm()
    return render(request, 'catalog/person.html', {
        'person_form': person_form,
    })


def person_with_id(request, pk):
    answer = None
    if request.method == 'POST':
        person_data = PersonForm(request.POST)
        if person_data.is_valid():
            data = person_data.cleaned_data
            Person.objects.filter(id=pk).update(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email']
            )
            answer = True
    db_user = get_object_or_404(Person, pk=pk)
    person_form = PersonForm(instance=db_user)
    return render(request, 'catalog/person_id.html', {
        'person_form': person_form,
        'pk': pk,
        'answer': answer,
    })

