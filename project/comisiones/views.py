from django.shortcuts import render, redirect
from cursos import models, forms

def home(request):
    consulta = request.GET.get("consulta", None)
    
    if consulta:
        query = models.Comision.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Comision.objects.all()
    
    context = {"comisiones" : query}
    return render(request, "comisiones/index.html", context)

