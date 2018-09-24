from django.conf.urls import url
from apps.crud_alumnos.views import alumnosCreate, alumnosList

urlpatterns = [
    url(r'^nuevo/', alumnosCreate.as_view(), name='alumno_crear'),
    url(r'^listar/', alumnosList.as_view(), name='alumnos_listar'),
]