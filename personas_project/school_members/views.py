from django.shortcuts import render, redirect
from .formulario import newAlumnoForm, newProfesorForm, newCicloForm
from .models import alumno, profesor, ciclo

# Create your views here.

def alumno_lista(request):
    context = {'listado' : alumno.objects.all()}
    return render(request, "school_members/alumno_listado.html", context)

def alumno_editar(request, id=0):
    if request.method == "GET":
        if id==0:
            form = newAlumnoForm()
        else:
            alumnoi = alumno.objects.get(pk=id)
            form = newAlumnoForm(instance=alumnoi)

        return render(request, "school_members/alumno_editar.html",{"form": form})
    else:
        if id==0:
            form = newAlumnoForm(request.POST)
        else:
            alumnoi = alumno.objects.get(pk=id)
            form = newAlumnoForm(request.POST, instance=alumnoi)
        if form.is_valid():
            form.save()
        return redirect('/alumno/listado')
def alumno_eliminar(request, id):
    alumnoi = alumno.objects.get(pk=id)
    alumnoi.delete()
    return redirect('/alumno/listado')



def profesor_lista(request):
    context = {'listado' : profesor.objects.all()}
    return render(request, "school_members/profesor_listado.html", context)

def profesor_editar(request, id=0):
    if request.method == "GET":
        if id==0:
            form = newProfesorForm()
        else:
            profesori = profesor.objects.get(pk=id)
            form = newProfesorForm(instance=profesori)

        return render(request, "school_members/profesor_editar.html",{"form": form})
    else:
        if id==0:
            form = newProfesorForm(request.POST)
        else:
            profesori = profesor.objects.get(pk=id)
            form = newProfesorForm(request.POST, instance=profesori)
        if form.is_valid():
            form.save()
        return redirect('/profesor/listado')
def profesor_eliminar(request, id):
    profesori = profesor.objects.get(pk=id)
    profesori.delete()
    return redirect('/profesor/listado')



def ciclo_lista(request):
    context = {'listado' : ciclo.objects.all()}
    return render(request, "school_members/ciclo_listado.html", context)

def ciclo_editar(request, id=0):
    if request.method == "GET":
        if id==0:
            form = newCicloForm()
        else:
            cicloi = ciclo.objects.get(pk=id)
            form = newCicloForm(instance=cicloi)

        return render(request, "school_members/ciclo_editar.html",{"form": form})
    else:
        if id==0:
            form = newCicloForm(request.POST)
        else:
            cicloi = ciclo.objects.get(pk=id)
            form = newCicloForm(request.POST, instance=cicloi)
        if form.is_valid():
            form.save()
        return redirect('/ciclo/listado')
def ciclo_eliminar(request, id):
    cicloi = ciclo.objects.get(pk=id)
    cicloi.delete()
    return redirect('/ciclo/listado')