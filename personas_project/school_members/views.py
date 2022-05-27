from django.shortcuts import render

# Create your views here.

def alumno_lista(request):
    return render(request, "school_members/alumno_listado.html")

def alumno_editar(request):
    return render(request, "school_members/alumno_editar.html")

def alumno_eliminar(request):
    return