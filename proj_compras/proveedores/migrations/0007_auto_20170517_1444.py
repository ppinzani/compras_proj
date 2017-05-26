# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0006_auto_20170517_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta',
            field=models.DateField(default=datetime.datetime(2017, 5, 17, 14, 44, 56, 607810, tzinfo=utc), blank=True),
        ),
    ]
