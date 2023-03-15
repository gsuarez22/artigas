from django.db import models

# Create your models here.

# Productos {id,nombre,stock,descripcion,foto,barra,vto, código, familia, grupo, tipo_impuesto}
# tipo_impuesto: 10  22  0
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

# Entradas_Productos {id,id_producto,proveedor,fecha_entrada,cantidad,costo_compra,costo_unitario, numero_factura}
class entrada_producto(models.Model):
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    proveedor=models.CharField(max_length=100)
    fecha_entrada=models.DateField()
    cantidad=models.IntegerField()
    costo_compra=models.DecimalField(max_digits=11,decimal_places=2)
    costo_unitario=models.DecimalField(max_digits=11,decimal_places=2)
    numero_factura=models.CharField(max_length=20)

# Movimientos_productos {id, id_producto, cantidad, fecha_movimiento, tipo, numero_referencia}   tipo: Factura, Compra, Inicial    numero_refencia: linea_factura o id entrada Producto, vacio si es inicial
class movimiento_producto(models.Model):
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    fecha_movimiento=models.DateField()
    tipo=models.CharField(max_length=10)
    proveedor=models.CharField(max_length=100)
    numero_referencia=models.CharField(max_length=20)
