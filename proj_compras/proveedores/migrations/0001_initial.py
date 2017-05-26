# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactoProveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=80, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('telefono_1', models.CharField(max_length=40, blank=True)),
                ('telefono_2', models.CharField(max_length=40, blank=True)),
                ('direccion_1', models.CharField(max_length=80, blank=True)),
                ('direccion_2', models.CharField(max_length=80, blank=True)),
                ('url', models.URLField(blank=True)),
                ('detalles', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(max_length=22, blank=True, unique=True, editable=False)),
                ('nombre_fiscal', models.CharField(max_length=100)),
                ('nombre_fantasia', models.CharField(max_length=100, blank=True)),
                ('fecha_alta', models.DateField(blank=True, default=datetime.datetime(2017, 5, 8, 23, 44, 6, 164563, tzinfo=utc))),
                ('cuit', models.CharField(max_length=25, blank=True)),
                ('margen_ganancia', models.SmallIntegerField(blank=True, null=True)),
                ('condicion_iva', models.CharField(max_length=5, default='RI', choices=[('CF', 'Consumidor Final'), ('RI', 'IVA Responsable Inscripto'), ('RNI', 'IVA Responsable No Inscripto'), ('MONO', 'Monotributo'), ('OTRO', 'Otro')])),
                ('contacto', models.ForeignKey(null=True, to='proveedores.ContactoProveedor', blank=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'verbose_name_plural': 'proveedores',
            },
        ),
    ]
