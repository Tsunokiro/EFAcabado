from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    precio_compra=models.CharField(max_length=20)
    precio_venta=models.CharField(max_length=20)
    fecha_compra=models.DateField()
    fecha_registro=models.DateField(auto_now_add=True)
    estado=models.CharField(max_length=6)

class Curso(models.Model):
    codigo=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    horas=models.IntegerField(max_length=5)
    creditos=models.IntegerField(max_length=5)
    fecha_registro=models.DateField(auto_now_add=True)
    estado=models.CharField(max_length=6)