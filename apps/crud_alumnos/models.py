from django.db import models

# Create your models here.

class carreras(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nombre)

class alumnos(models.Model):
    nocontrol = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    carreras = models.ForeignKey(carreras, null=True, blank=True, on_delete=models.CASCADE)

# Paso 8. Ejecutar el comando para realizar la migración del modelo
# a la base de datos
#
# python3 manage.py makemigrations
# python3 manage.py migrate

# Paso 9. Insertar datos a la base de datos python3 manage.py shell
# from apps.crud_alumnos.models import carreras

# d = carreras(id = 1, nombre = 'Ingeniería en informática')
# d.save()