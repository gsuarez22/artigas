# Generated by Django 4.1.6 on 2023-03-15 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_facturacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='id_cliente',
        ),
    ]
