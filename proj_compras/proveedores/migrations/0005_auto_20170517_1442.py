# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0004_auto_20170517_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta',
            field=models.DateField(default=datetime.datetime(2017, 5, 17, 14, 42, 1, 869778, tzinfo=utc), blank=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre_fantasia',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
