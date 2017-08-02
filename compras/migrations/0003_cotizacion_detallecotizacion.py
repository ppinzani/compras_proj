# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercaderias', '0001_initial'),
        ('compras', '0002_auto_20170614_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('fecha_generada', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cotizacion',
                'verbose_name_plural': 'Cotizaciones',
            },
        ),
        migrations.CreateModel(
            name='DetalleCotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(max_digits=20, decimal_places=5)),
                ('cotizacion', models.ForeignKey(to='compras.Cotizacion')),
                ('mercaderia', models.ForeignKey(to='mercaderias.Mercaderia')),
            ],
            options={
                'verbose_name': 'DetalleSolicitud',
                'verbose_name_plural': 'DetallesSolicitud',
            },
        ),
    ]
