from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.asignatura_editar, name='asignatura_insertar'),
    path('<int:id>/', views.asignatura_editar, name='asignatura_actualizar'),
    path('delete/<int:id>/', views.asignatura_eliminar, name='asignatura_eliminar'),
    path('listado/', views.asignatura_lista, name='asignatura_listado')
]

