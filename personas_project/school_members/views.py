from django.shortcuts import render, redirect
from .formulario import newAlumnoForm, newProfesorForm, newCicloForm, newAsignaturaForm
from .models import alumno, profesor, ciclo, asignatura
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




#----------------------------------------------Métodos de login y logout----------------------------------------------

#Método de login

def login_user(request):
    if request.method == "POST":
        user = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user, password=password)
        if user is not None:
            login(request, user)
            return redirect('/alumno/listado')
        else:
            return redirect('/')
    else:
        return render(request, "school_members/main.html", {})

#Método de logout

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def logout_user(request):
    logout(request)
    return redirect('/')




#----------------------------------------------------Métodos de alumno-----------------------------------------------------

#Método para listar a los alumnos

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def alumno_lista(request):
    context = {'listado' : alumno.objects.all().order_by('apellidos')}
    return render(request, "school_members/alumno_listado.html", context)

#Método para mostrar el formualario de creación de alumnos que a su vez sirve para modificar los datos de los mismos

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
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
            form = newAlumnoForm(request.POST, request.FILES)
        else:
            alumnoi = alumno.objects.get(pk=id)
            form = newAlumnoForm(request.POST,request.FILES, instance=alumnoi)
        if form.is_valid():
            form.save()
        return redirect('/alumno/listado')

#Método para eliminar un alumno
        
@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def alumno_eliminar(request, id):
    alumnoi = alumno.objects.get(pk=id)
    alumnoi.delete()
    return redirect('/alumno/listado')

#Método para acceder a los detalles del alumno

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def alumno_detalles(request, id):
    alumnoi = alumno.objects.get(id=id) 
    return render(request, "school_members/alumno_detalles.html", {'data':alumnoi})




#----------------------------------------------------Métodos de profesor---------------------------------------------------------

#Método para listar a los profesores

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def profesor_lista(request):
    context = {'listado' : profesor.objects.all().order_by('apellidos')}
    return render(request, "school_members/profesor_listado.html", context)

#Método para mostrar el formualario de creación de profesores que a su vez sirve para modificar los datos de los mismos

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
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
            form = newProfesorForm(request.POST, request.FILES)
        else:
            profesori = profesor.objects.get(pk=id)
            form = newProfesorForm(request.POST,request.FILES, instance=profesori)
        if form.is_valid():
            form.save()
        return redirect('/profesor/listado')

#Método para eliminar un profesor

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def profesor_eliminar(request, id):
    profesori = profesor.objects.get(pk=id)
    profesori.delete()
    return redirect('/profesor/listado')

#Método para acceder a los detalles del profesor

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def profesor_detalles(request, id):
    asignaturai = asignatura.objects.filter(profesor=id).values()
    profesori = profesor.objects.get(id=id) 
    return render(request, "school_members/profesor_detalles.html", {'data':profesori, 'data2':asignaturai})




#----------------------------------------------------Métodos de ciclo---------------------------------------------------------

#Método para listar los ciclos

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def ciclo_lista(request):
    context = {'listado' : ciclo.objects.all().order_by('nombre')}
    return render(request, "school_members/ciclo_listado.html", context)

#Método para mostrar el formualario de creación de ciclos que a su vez sirve para modificar los datos de los mismos

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
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

#Método para eliminar un ciclo

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def ciclo_eliminar(request, id):
    cicloi = ciclo.objects.get(pk=id)
    cicloi.delete()
    return redirect('/ciclo/listado')

#Método para acceder a los detalles del ciclo

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def ciclo_detalles(request, id):
    alumnosi = alumno.objects.filter(ciclo=id).values()
    asignaturai = asignatura.objects.filter(ciclo=id).values()
    return render(request, "school_members/ciclo_detalles.html",{'data':asignaturai, 'data2':alumnosi} )




#----------------------------------------------------Métodos de asignatura---------------------------------------------------------

#Método para listar las asignaturas

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def asignatura_lista(request):
    context = {'listado' : asignatura.objects.all().order_by('ciclo')}
    return render(request, "school_members/asignatura_listado.html", context)

#Método para mostrar el formualario de creación de asignaturas que a su vez sirve para modificar los datos de las mismas

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def asignatura_editar(request, id=0):
    if request.method == "GET":
        if id==0:
            form = newAsignaturaForm()
        else:
            asignaturai = asignatura.objects.get(pk=id)
            form = newAsignaturaForm(instance=asignaturai)
        return render(request, "school_members/asignatura_editar.html",{"form": form})
    else:
        if id==0:
            form = newAsignaturaForm(request.POST)
        else:
            asignaturai = asignatura.objects.get(pk=id)
            form = newAsignaturaForm(request.POST, instance=asignaturai)
        if form.is_valid():
            form.save()
        return redirect('/asignatura/listado')

#Método para eliminar una asignatura

@login_required(login_url="/") #Bloquea el acceso a este metodo si no se está logeado
def asignatura_eliminar(request, id):
    asignaturai = asignatura.objects.get(pk=id)
    asignaturai.delete()
    return redirect('/asignatura/listado')
