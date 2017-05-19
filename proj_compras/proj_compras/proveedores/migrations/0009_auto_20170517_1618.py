# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0008_auto_20170517_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactoproveedor',
            name='proveedor',
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 17, 16, 18, 7, 5943, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='ContactoProveedor',
        ),
    ]
