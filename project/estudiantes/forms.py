from django import forms
from cursos import models

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = ['nombre']
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
        }
