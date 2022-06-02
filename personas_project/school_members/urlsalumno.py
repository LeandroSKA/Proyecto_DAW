from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.alumno_editar, name='alumnos_insertar'),
    path('<int:id>/', views.alumno_editar, name='alumnos_actualizar'),
    path('delete/<int:id>/', views.alumno_eliminar, name='alumnos_eliminar'),
    path('listado/', views.alumno_lista, name='alumnos_listado'),
    path('detalles/<int:id>/', views.alumno_detalles, name='alumno_detalles')
]