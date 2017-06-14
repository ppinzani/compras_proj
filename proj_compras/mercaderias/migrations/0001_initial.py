# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaMercaderia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('padre', models.OneToOneField(to='mercaderias.CategoriaMercaderia', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Categoria De Mercaderia',
                'verbose_name_plural': 'Categorias de Mercaderia',
            },
        ),
        migrations.CreateModel(
            name='Mercaderia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(blank=True, max_length=100)),
                ('categoria', models.ManyToManyField(to='mercaderias.CategoriaMercaderia', blank=True)),
            ],
            options={
                'verbose_name': 'Mercaderia',
                'verbose_name_plural': 'Mercaderias',
            },
        ),
    ]
