# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0014_ordendecompra_cuotas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordendecompra',
            name='factura',
        ),
        migrations.AddField(
            model_name='facturadecompra',
            name='orden',
            field=models.OneToOneField(null=True, to='compras.OrdenDeCompra'),
        ),
        migrations.AlterField(
            model_name='ordendecompra',
            name='forma_de_pago',
            field=models.CharField(choices=[('E', 'Contado Efectivo'), ('C', 'En cuotas')], max_length=5, blank=True),
        ),
    ]
