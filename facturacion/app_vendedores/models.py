from django.db import models

# Create your models here.

class vendedor(models.Model):
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    email=models.EmailField(max_length=255)
    porcentaje_comision = models.IntegerField()    
    fecha_ingreso=models.DateField()
    usuario=models.CharField(max_length=8, unique=True)
    clave=models.CharField(max_length=12)        