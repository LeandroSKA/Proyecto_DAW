from distutils.command.upload import upload
from pickle import TRUE
from django.db import models


class ciclo(models.Model):
    nombre= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class profesor(models.Model):
    DNI= models.CharField(max_length=9)
    nombre= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=100)
    numero= models.CharField(max_length=15)
    correo= models.CharField(max_length=100)
    residencia= models.CharField(max_length=200)
    foto = models.ImageField(null=True, blank=True, upload_to= "profesores/")
    def __str__(self):
        return self.nombre
    

class alumno(models.Model):
    DNI= models.CharField(max_length=9)
    nombre= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=100)
    numero= models.CharField(max_length=15)
    correo= models.CharField(max_length=100)
    residencia= models.CharField(max_length=200)
    foto = models.ImageField(null=True, blank=True, upload_to= "alunnos/")
    ciclo= models.ForeignKey(ciclo,on_delete=models.CASCADE)

class asignatura(models.Model):
    nombre= models.CharField(max_length=100)
    horas = models.IntegerField(default=0)
    profesor= models.ForeignKey(profesor,on_delete=models.CASCADE)
    ciclo= models.ForeignKey(ciclo,on_delete=models.CASCADE)
