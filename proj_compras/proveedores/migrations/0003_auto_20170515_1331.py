# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_auto_20170511_0417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='contacto',
        ),
        migrations.AddField(
            model_name='contactoproveedor',
            name='proveedor',
            field=models.ForeignKey(to='proveedores.Proveedor', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactoproveedor',
            name='nombre',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='condicion_iva',
            field=models.CharField(default='NE', choices=[('CF', 'Consumidor Final'), ('NE', 'No Especifica'), ('RI', 'IVA Responsable Inscripto'), ('RNI', 'IVA Responsable No Inscripto'), ('MONO', 'Monotributo'), ('OTRO', 'Otro')], max_length=5),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_alta',
            field=models.DateField(default=datetime.datetime(2017, 5, 15, 13, 31, 32, 713894, tzinfo=utc), blank=True),
        ),
    ]
