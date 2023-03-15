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

class tarjeta(models.Model):
    id_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    numero=models.CharField(max_length=16)
    vto=models.DateField()
    cod_verificador=models.CharField(max_length=4)
    operador=models.CharField(max_length=50)
    precargado=models.CharField(max_length=2)

