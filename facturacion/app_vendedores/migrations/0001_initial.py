# Generated by Django 4.1.6 on 2023-03-10 18:28

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
                ('email', models.EmailField(max_length=255)),
                ('porcentaje_comision', models.IntegerField()),
                ('fecha_ingreso', models.DateField()),
                ('usuario', models.CharField(max_length=8, unique=True)),
                ('clave', models.CharField(max_length=12)),
            ],
        ),
    ]
