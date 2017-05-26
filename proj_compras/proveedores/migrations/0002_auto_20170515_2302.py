# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 15, 23, 2, 1, 498004, tzinfo=utc)),
        ),
    ]
