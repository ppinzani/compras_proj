# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0003_auto_20170516_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
