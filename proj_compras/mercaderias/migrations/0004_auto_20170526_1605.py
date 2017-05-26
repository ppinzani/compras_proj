# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercaderias', '0003_auto_20170526_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriamercaderia',
            name='subcategoria',
            field=models.OneToOneField(null=True, to='mercaderias.CategoriaMercaderia', blank=True),
        ),
        migrations.AlterField(
            model_name='mercaderia',
            name='categoria',
            field=models.ManyToManyField(blank=True, null=True, to='mercaderias.CategoriaMercaderia'),
        ),
    ]
