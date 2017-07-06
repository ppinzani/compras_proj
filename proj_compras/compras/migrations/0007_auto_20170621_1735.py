# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mercaderias', '0001_initial'),
        ('compras', '0006_cotizacion_modificado_por'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleOrdenCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(max_digits=15, decimal_places=3)),
                ('mercaderia', models.ForeignKey(to='mercaderias.Mercaderia')),
            ],
            options={
                'verbose_name_plural': 'DetallesOrdenDeCompra',
                'verbose_name': 'DetalleOrdenDeCompra',
            },
        ),
        migrations.CreateModel(
            name='FacturaDeCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('fecha', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('importe', models.DecimalField(max_digits=15, decimal_places=3)),
                ('foto', models.ImageField(blank=True, upload_to='facturas_de_compra')),
            ],
            options={
                'verbose_name_plural': 'FacturasDeCompra',
                'verbose_name': 'FacturaDeCompra',
            },
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('forma_de_pago', models.CharField(max_length=5, choices=[('E', 'Contado Efectivo'), ('C', 'En cuotas')], default='Pe')),
            ],
            options={
                'verbose_name_plural': 'OrdenesDeCompra',
                'verbose_name': 'OrdenDeCompra',
            },
        ),
        migrations.CreateModel(
            name='PagoDeCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('fecha_de_pago', models.DateTimeField(null=True, blank=True)),
                ('importe', models.DecimalField(max_digits=15, decimal_places=3)),
                ('estado', models.CharField(max_length=5, choices=[('Pa', 'Pagado'), ('Pe', 'Pendiente')], default='E')),
                ('orden', models.ForeignKey(to='compras.OrdenDeCompra')),
            ],
            options={
                'verbose_name_plural': 'PagosDeCompra',
                'verbose_name': 'PagoDeCompra',
            },
        ),
        migrations.AlterModelOptions(
            name='cotizacion',
            options={'verbose_name_plural': 'Cotizaciones', 'permissions': (('puede_aprobar_orden_de_compra', 'Puede aprobar las cotizaciones pendientes'),), 'verbose_name': 'Cotizacion'},
        ),
        migrations.AlterModelOptions(
            name='detallecotizacion',
            options={'verbose_name_plural': 'DetallesSolicitud', 'verbose_name': 'DetalleOrdenCompra'},
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='estado',
            field=models.CharField(max_length=5, choices=[('A', 'Aprobada'), ('P', 'Pendiente'), ('R', 'Rechazada')], default='P'),
        ),
        migrations.AlterField(
            model_name='detallecotizacion',
            name='precio',
            field=models.DecimalField(max_digits=15, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='solicituddecompra',
            name='estado',
            field=models.CharField(max_length=5, choices=[('A', 'Aprobada'), ('P', 'Pendiente'), ('R', 'Rechazada')], default='P'),
        ),
        migrations.AddField(
            model_name='ordendecompra',
            name='cotizacion',
            field=models.ForeignKey(to='compras.Cotizacion'),
        ),
        migrations.AddField(
            model_name='detalleordencompra',
            name='orden',
            field=models.ForeignKey(to='compras.Cotizacion'),
        ),
    ]
