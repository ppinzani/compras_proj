# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_auto_20170619_1122'),
        ('mercaderias', '0002_auto_20170712_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='MercaderiaProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('ultimo_precio', models.DecimalField(blank=True, max_digits=15, decimal_places=2)),
                ('mercaderia', models.ForeignKey(to='mercaderias.Mercaderia')),
                ('proveedor', models.ForeignKey(to='proveedores.Proveedor')),
            ],
            options={
                'verbose_name_plural': 'MercaderiasProveedores',
                'verbose_name': 'MercaderiaProveedor',
            },
        ),
    ]
