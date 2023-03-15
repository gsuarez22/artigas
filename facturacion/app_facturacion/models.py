from django.db import models
import app_vendedores
import app_clientes


# Create your models here.

# Facturas {id, id_cliente, fecha, importe_subtotal, importe_impuesto, Importe_total,  numero_factura_dgi, tipo_comprobante, id_vendedor} tipo_comprobante: Eticket, Efactura, Efacturanotacredito, eticketnotacredito 
class factura(models.Model):
    id_cliente = models.ForeignKey(app_clientes.models.cliente, on_delete=models.CASCADE, blank=True, null=True)
    #id_vendedor = models.ForeignKey(app_vendedores.models.vendedor, on_delete=models.CASCADE)
    fecha=models.DateField()
    importe_subtotal=models.DecimalField(max_digits=12,decimal_places=2)
    importe_impuesto=models.DecimalField(max_digits=12,decimal_places=2)
    importe_total=models.DecimalField(max_digits=12,decimal_places=2)
    numero_factura_dgi=models.CharField(max_length=20)
    tipo_comprobante=models.CharField(max_length=40)
    


# Lineas_Facturas {id, id_factura, id_producto, cantidad, importe_subtotal, importe_impuesto, Importe_total, tipo_impuesto} tipo_impuesto: 10  22  0


# Comisiones {id, vendedor, id_factura, porcentaje, importe_a_pagar, importe_pago, fecha_pago, estado}
