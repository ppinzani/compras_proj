# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0010_auto_20170629_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='descuento',
            field=models.PositiveIntegerField(null=True, default=0, blank=True),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='iva',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
