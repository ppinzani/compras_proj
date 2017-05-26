# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0009_auto_20170517_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(unique=True, max_length=22, editable=False, blank=True)),
                ('nombre', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('telefono', models.CharField(max_length=40, blank=True)),
                ('direccion', models.CharField(max_length=80, blank=True)),
                ('pagina_web', models.URLField(blank=True)),
                ('detalles', models.TextField(blank=True)),
                ('proveedor', models.ForeignKey(null=True, blank=True, to='proveedores.Proveedor')),
            ],
            options={
                'verbose_name_plural': 'contactos',
            },
        ),
    ]
