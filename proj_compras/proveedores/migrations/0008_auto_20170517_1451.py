# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0007_auto_20170517_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta',
            field=models.DateField(default=datetime.datetime(2017, 5, 17, 14, 51, 0, 469503, tzinfo=utc), blank=True),
        ),
    ]
