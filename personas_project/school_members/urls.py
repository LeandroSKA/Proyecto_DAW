from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.alumno_editar, name='alumnos_insertar'),
    path('<int:id>/', views.alumno_editar, name='alumnos_actualizar'),
    path('listado/', views.alumno_lista, name='alumnos_listado')
]
