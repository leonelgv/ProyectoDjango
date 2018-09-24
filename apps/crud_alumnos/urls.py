from django.conf.urls import url
from apps.crud_alumnos.views import alumnosCreate

urlpatterns = [
    url(r'^nuevo/', alumnosCreate.as_view(), name='alumno_crear'),
]