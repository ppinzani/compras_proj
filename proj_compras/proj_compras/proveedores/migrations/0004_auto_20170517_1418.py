# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0003_auto_20170515_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta',
            field=models.DateField(default=datetime.datetime(2017, 5, 17, 14, 18, 48, 749065, tzinfo=utc), blank=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre_fantasia',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
