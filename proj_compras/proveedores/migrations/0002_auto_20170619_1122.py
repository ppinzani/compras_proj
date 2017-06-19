# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='nombre_fantasia',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre_fiscal',
            field=models.CharField(max_length=80),
        ),
    ]
