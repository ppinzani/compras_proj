# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0008_auto_20170621_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleordencompra',
            name='mercaderia',
        ),
        migrations.RemoveField(
            model_name='detalleordencompra',
            name='orden',
        ),
        migrations.AddField(
            model_name='facturadecompra',
            name='tipo',
            field=models.CharField(choices=[('A', 'Factura A'), ('B', 'Factura B'), ('C', 'Factura C')], default='A', max_length=5),
        ),
        migrations.AlterField(
            model_name='ordendecompra',
            name='forma_de_pago',
            field=models.CharField(blank=True, choices=[('E', 'Contado Efectivo'), ('C', 'En cuotas')], null=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='pagodecompra',
            name='estado',
            field=models.CharField(choices=[('Pa', 'Pagado'), ('Pe', 'Pendiente')], default='Pe', max_length=5),
        ),
        migrations.AlterField(
            model_name='solicituddecompra',
            name='estado',
            field=models.CharField(choices=[('A', 'Aprobada'), ('P', 'Pendiente')], default='P', max_length=5),
        ),
        migrations.DeleteModel(
            name='DetalleOrdenCompra',
        ),
    ]
