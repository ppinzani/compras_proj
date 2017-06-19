# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_auto_20170618_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecotizacion',
            name='precio',
            field=models.DecimalField(max_digits=20, decimal_places=3),
        ),
    ]
