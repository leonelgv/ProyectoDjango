# Paso 11. Crear una vista
# Paso 12. Agregar a la carpeta static los archivos css y js del framework
#          materialize
# Paso 13. Crear las carpetas 'base' y 'crudalumnos' en la carpeta templates
# Paso 14. Crear los archivos base.html y alumnos_form.html y guardarlos en
#          las carpetas 'base' y 'crudalumnos' respectivamente
from django.shortcuts import render
from django.views.generic import CreateView
from apps.crud_alumnos.models import alumnos
from apps.crud_alumnos.forms import alumnosForm

# Create your views here.

class alumnosCreate(CreateView):
    model = alumnos
    form_class = alumnosForm
    template_name = 'crudalumnos/alumnos_form.html'