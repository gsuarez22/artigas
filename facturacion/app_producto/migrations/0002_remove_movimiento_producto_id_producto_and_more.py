# Generated by Django 4.1.6 on 2023-04-23 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_producto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimiento_producto',
            name='id_producto',
        ),
        migrations.RemoveField(
            model_name='precio_producto',
            name='id_producto',
        ),
        migrations.DeleteModel(
            name='entrada_producto',
        ),
        migrations.DeleteModel(
            name='movimiento_producto',
        ),
        migrations.DeleteModel(
            name='precio_producto',
        ),
        migrations.DeleteModel(
            name='producto',
        ),
    ]
