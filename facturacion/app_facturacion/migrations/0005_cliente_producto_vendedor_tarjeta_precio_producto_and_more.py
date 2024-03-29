# Generated by Django 4.1.6 on 2023-04-23 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_facturacion', '0004_factura_id_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('rut', models.CharField(max_length=12)),
                ('cedula', models.CharField(max_length=8, unique=True)),
                ('direccion', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('detalle', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('foto', models.CharField(max_length=255)),
                ('barra', models.IntegerField()),
                ('vto', models.DateField()),
                ('codigo', models.CharField(max_length=50)),
                ('familia', models.CharField(max_length=255)),
                ('grupo', models.CharField(max_length=255)),
                ('tipo_impuesto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=255)),
                ('porcentaje_comision', models.IntegerField()),
                ('fecha_ingreso', models.DateField()),
                ('usuario', models.CharField(max_length=8, unique=True)),
                ('clave', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=16)),
                ('vto', models.DateField()),
                ('cod_verificador', models.CharField(max_length=4)),
                ('operador', models.CharField(max_length=50)),
                ('precargado', models.CharField(max_length=2)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_facturacion.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='precio_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=11)),
                ('tipo', models.CharField(max_length=10)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_facturacion.producto')),
            ],
        ),
        migrations.CreateModel(
            name='movimiento_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha_movimiento', models.DateField()),
                ('tipo', models.CharField(max_length=10)),
                ('proveedor', models.CharField(max_length=100)),
                ('numero_referencia', models.CharField(max_length=20)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_facturacion.producto')),
            ],
        ),
        migrations.CreateModel(
            name='entrada_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.CharField(max_length=100)),
                ('fecha_entrada', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('costo_compra', models.DecimalField(decimal_places=2, max_digits=11)),
                ('costo_unitario', models.DecimalField(decimal_places=2, max_digits=11)),
                ('numero_factura', models.CharField(max_length=20)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_facturacion.producto')),
            ],
        ),
        migrations.AlterField(
            model_name='factura',
            name='id_cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_facturacion.cliente'),
        ),
    ]
