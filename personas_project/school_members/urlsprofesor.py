from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profesor_editar, name='profesor_insertar'),
    path('<int:id>/', views.profesor_editar, name='profesor_actualizar'),
    path('delete/<int:id>/', views.profesor_eliminar, name='profesor_eliminar'),
    path('listado/', views.profesor_lista, name='profesor_listado'),
    path('detalles/<int:id>/', views.profesor_detalles, name='profesor_detalles')
]
