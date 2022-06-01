from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ciclo_editar, name='ciclo_insertar'),
    path('<int:id>/', views.ciclo_editar, name='ciclo_actualizar'),
    path('delete/<int:id>/', views.ciclo_eliminar, name='ciclo_eliminar'),
    path('listado/', views.ciclo_lista, name='ciclo_listado')
]
