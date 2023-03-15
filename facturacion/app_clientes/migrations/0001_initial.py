# Generated by Django 4.1.5 on 2023-02-14 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
    ]