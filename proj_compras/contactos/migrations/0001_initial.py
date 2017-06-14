# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, unique=True, editable=False, max_length=22)),
                ('nombre', models.CharField(max_length=80)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=40)),
                ('direccion', models.CharField(blank=True, max_length=80)),
                ('pagina_web', models.URLField(blank=True)),
                ('detalles', models.TextField(blank=True)),
                ('proveedor', models.ForeignKey(blank=True, null=True, to='proveedores.Proveedor')),
            ],
            options={
                'verbose_name_plural': 'contactos',
            },
        ),
    ]
