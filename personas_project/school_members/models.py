from django.db import models

# Create your models here.

class ciclo(models.Model):
    nombre= models.CharField(max_length=50)

class profesor(models.Model):
    DNI= models.CharField(max_length=9,primary_key=True)
    nombre= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=100)
    numero= models.CharField(max_length=15)
    correo= models.CharField(max_length=100)
    fecha= models.DateField()
    foto= models.ImageField(upload_to ='imagenes/')
    residencia= models.CharField(max_length=200)

class alumno(models.Model):
    DNI= models.CharField(max_length=9,primary_key=True)
    nombre= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=100)
    numero= models.CharField(max_length=15)
    correo= models.CharField(max_length=100)
    fecha= models.DateField()
    foto= models.ImageField(upload_to ='imagenes/')
    residencia= models.CharField(max_length=200)
    ciclo= models.ForeignKey(ciclo,on_delete=models.CASCADE)

class asignatura(models.Model):
    nombre= models.CharField(max_length=50)
    profesor= models.ForeignKey(profesor,on_delete=models.CASCADE)
    ciclo= models.ForeignKey(ciclo,on_delete=models.CASCADE)
