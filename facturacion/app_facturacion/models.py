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

class factura(models.Model):
    id_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, blank=True, null=True)
    #id_vendedor = models.ForeignKey(app_vendedores.models.vendedor, on_delete=models.CASCADE)
    fecha=models.DateField()
    importe_subtotal=models.DecimalField(max_digits=12,decimal_places=2)
    importe_impuesto=models.DecimalField(max_digits=12,decimal_places=2)
    importe_total=models.DecimalField(max_digits=12,decimal_places=2)
    numero_factura_dgi=models.CharField(max_length=20)
    tipo_comprobante=models.CharField(max_length=40)
    

class producto(models.Model):
    nombre=models.CharField(max_length=100)
    stock=models.IntegerField()
    descripcion=models.CharField(max_length=255)
    foto=models.CharField(max_length=255)
    barra=models.IntegerField()
    vto=models.DateField()
    codigo=models.CharField(max_length=50)
    familia=models.CharField(max_length=255)
    grupo=models.CharField(max_length=255)
    tipo_impuesto=models.IntegerField()
    
 
# Precios_Productos{id,id_producto,precio,tipo}    tipo=Mayor  Menor Especial
class precio_producto(models.Model):
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    precio=models.DecimalField(max_digits=11,decimal_places=2)
    tipo=models.CharField(max_length=10)

class entrada_producto(models.Model):
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    proveedor=models.CharField(max_length=100)
    fecha_entrada=models.DateField()
    cantidad=models.IntegerField()
    costo_compra=models.DecimalField(max_digits=11,decimal_places=2)
    costo_unitario=models.DecimalField(max_digits=11,decimal_places=2)
    numero_factura=models.CharField(max_length=20)

class movimiento_producto(models.Model):
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    fecha_movimiento=models.DateField()
    tipo=models.CharField(max_length=10)
    proveedor=models.CharField(max_length=100)
    numero_referencia=models.CharField(max_length=20)

class vendedor(models.Model):
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    email=models.EmailField(max_length=255)
    porcentaje_comision = models.IntegerField()    
    fecha_ingreso=models.DateField()
    usuario=models.CharField(max_length=8, unique=True)
    clave=models.CharField(max_length=12)        