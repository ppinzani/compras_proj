# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
        ('compras', '0003_cotizacion_detallecotizacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallecotizacion',
            options={'verbose_name_plural': 'DetallesSolicitud', 'permissions': (('puede_aprobar_cotizacion', 'Puede aprobar las cotizaciones pendientes'),), 'verbose_name': 'DetalleSolicitud'},
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='estado',
            field=models.CharField(max_length=5, default='P', choices=[('A', 'Aprobada'), ('P', 'Pendiente')]),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='proveedor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='proveedores.Proveedor'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='solicitud',
            field=models.ForeignKey(blank=True, null=True, to='compras.SolicitudDeCompra'),
        ),
        migrations.AlterField(
            model_name='solicituddecompra',
            name='estado',
            field=models.CharField(max_length=5, default='P', choices=[('A', 'Aprobada'), ('P', 'Pendiente')]),
        ),
    ]
