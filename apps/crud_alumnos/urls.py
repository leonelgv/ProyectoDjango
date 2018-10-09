from django.conf.urls import url
from apps.crud_alumnos.views import alumnosCreate, alumnosList, alumnosDelete, alumnosUpdate, alumnoShow, search

urlpatterns = [
    url(r'^nuevo/', alumnosCreate.as_view(), name='alumno_crear'),
    url(r'^listar/', alumnosList.as_view(), name='alumnos_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', alumnosDelete.as_view(), name='alumno_eliminar'),
    url(r'^modificar/(?P<pk>\d+)/$', alumnosUpdate.as_view(), name='alumno_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', alumnoShow.as_view(), name='alumno_mostrar'),
    url(r'^buscar/$', search, name='alumno_buscar'),
]