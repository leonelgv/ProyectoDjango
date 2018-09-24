from django import forms
from apps.crud_alumnos.models import alumnos

class alumnosForm(forms.ModelForm):
    class Meta:
        model = alumnos
        fields = [
            'nocontrol',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'fecha_nacimiento',
            'carreras'
        ]
        labels = {
            'nocontrol': 'Numero de Control',
            'nombre' : 'Nombres',
            'apellido_paterno': 'Apellido Paterno',
            'apellido_materno': 'Apellido Materno',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'carreras': 'Carrera'
        }

        widgets = {
            'nocontrol': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
            'carreras': forms.Select(attrs={'class':'form-control'}),
        }