from django.shortcuts import render
from django.views.generic import CreateView
from apps.crud_alumnos.models import alumnos
from apps.crud_alumnos.forms import alumnosForm

# Create your views here.

class alumnosCreate(CreateView):
    model = alumnos
    form_class = alumnosForm
    template_name = 'crudalumnos/alumnos_form.html'