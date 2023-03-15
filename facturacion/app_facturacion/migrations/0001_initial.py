# Generated by Django 4.1.6 on 2023-03-15 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_clientes', '0002_tarjeta'),
    ]

    operations = [
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('importe_subtotal', models.DecimalField(decimal_places=2, max_digits=11)),
                ('importe_impuesto', models.DecimalField(decimal_places=2, max_digits=11)),
                ('importe_total', models.DecimalField(decimal_places=2, max_digits=11)),
                ('numero_factura_dgi', models.CharField(max_length=20)),
                ('tipo_comprobante', models.CharField(max_length=40)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_clientes.cliente')),
            ],
        ),
    ]