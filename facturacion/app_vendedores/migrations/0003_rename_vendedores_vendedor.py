# Generated by Django 4.1.6 on 2023-03-15 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_vendedores', '0002_rename_cliente_vendedores'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='vendedores',
            new_name='vendedor',
        ),
    ]
