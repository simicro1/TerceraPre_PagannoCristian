from django.shortcuts import render

from cursos import models

def home(request):
    query = models.Comision.objects.all()
    context = {"comisiones" : query}
    return render(request, "comisiones/index.html", context)
