# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, unique=True, max_length=22)),
                ('nombre_fiscal', models.CharField(max_length=100)),
                ('nombre_fantasia', models.CharField(blank=True, max_length=100)),
                ('fecha_alta', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('cuit', models.CharField(blank=True, max_length=25)),
                ('margen_ganancia', models.SmallIntegerField(blank=True, null=True)),
                ('condicion_iva', models.CharField(default='NE', choices=[('CF', 'Consumidor Final'), ('NE', 'No Especifica'), ('RI', 'IVA Responsable Inscripto'), ('RNI', 'IVA Responsable No Inscripto'), ('MONO', 'Monotributo'), ('OTRO', 'Otro')], max_length=5)),
            ],
            options={
                'verbose_name_plural': 'proveedores',
            },
        ),
    ]
