# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0007_auto_20170621_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordendecompra',
            name='factura',
            field=models.OneToOneField(to='compras.FacturaDeCompra', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='ordendecompra',
            name='numero',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
    ]
