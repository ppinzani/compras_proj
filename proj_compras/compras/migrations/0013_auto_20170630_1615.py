# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0012_auto_20170630_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecotizacion',
            name='precio',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='facturadecompra',
            name='importe',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='pagodecompra',
            name='importe',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
    ]
