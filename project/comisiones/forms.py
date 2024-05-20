from django import forms
from cursos import models

class ComisionForm(forms.ModelForm):
    class Meta:
        model = models.Comision
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "curso": forms.Select(attrs={"class": "form-control"}),
            "profesor": forms.Select(attrs={"class": "form-control"}),
            "estudiante": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
