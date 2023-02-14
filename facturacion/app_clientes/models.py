from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    rut=models.CharField(max_length=12)
    cedula=models.CharField(max_length=8, unique=True)
    direccion=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    fecha_nacimiento=models.DateField()
    detalle=models.CharField(max_length=255)
