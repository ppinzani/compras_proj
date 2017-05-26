# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercaderias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaMercaderia',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('subcategoria', models.OneToOneField(to='mercaderias.CategoriaMercaderia')),
            ],
            options={
                'verbose_name': 'Categoria De Mercaderia',
                'verbose_name_plural': 'Categorias de Mercaderia',
            },
        ),
        migrations.AddField(
            model_name='mercaderia',
            name='categoria',
            field=models.ManyToManyField(blank=True, to='mercaderias.CategoriaMercaderia'),
        ),
    ]
