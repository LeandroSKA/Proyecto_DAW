from django.shortcuts import render, redirect
from .formulario import newPeopleForm
from .models import alumno

# Create your views here.

def alumno_lista(request):
    context = {'listado' : alumno.objects.all()}
    return render(request, "school_members/alumno_listado.html", context)

def alumno_editar(request, id=0):
    if request.method == "GET":
        if id==0:
            form = newPeopleForm()
        else:
            alumnoi = alumno.objects.get(pk=id)
            form = newPeopleForm(instance=alumnoi)

        return render(request, "school_members/alumno_editar.html",{"form": form})
    else:
        if id==0:
            form = newPeopleForm(request.POST)
        else:
            alumnoi = alumno.objects.get(pk=id)
            form = newPeopleForm(request.POST, instance=alumnoi)
        if form.is_valid():
            form.save()
        return redirect('/alumno/listado')
def alumno_eliminar(request, id):
    alumnoi = alumno.objects.get(pk=id)
    alumnoi.delete()
    return redirect('/alumno/listado')

