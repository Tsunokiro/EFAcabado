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