from django.shortcuts import render

from cursos import models

def home(request):
    consulta = request.GET.get("consulta", None)
    
    if consulta:
        query = models.Profesor.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Profesor.objects.all()
    context = {"profesores" : query}
    return render(request, "profesores/index.html", context)

