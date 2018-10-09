import django_filters
from apps.crud_alumnos.models import alumnos

class alumnosFilter(django_filters.FilterSet):
    class Meta:
        model = alumnos
        fields = ['nocontrol', 'nombre', 'carreras']