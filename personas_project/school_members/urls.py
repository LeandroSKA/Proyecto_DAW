from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.alumno_editar),
    path('listado/', views.alumno_lista)
]
