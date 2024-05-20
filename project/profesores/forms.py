from django import forms
from cursos import models

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = models.Profesor
        fields = ['nombre']
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
        }
