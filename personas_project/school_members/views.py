from django.shortcuts import render, redirect
from .formulario import newPeopleForm
from .models import alumno

# Create your views here.

def alumno_lista(request):
    context = {'listado' : alumno.objects.all()}
    return render(request, "school_members/alumno_listado.html", context)

def alumno_editar(request):
    if request.method == "GET":
        form = newPeopleForm()
        return render(request, "school_members/alumno_editar.html",{"form": form})
    else:
        form = newPeopleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/alumno/listado')
def alumno_eliminar(request):
    return

