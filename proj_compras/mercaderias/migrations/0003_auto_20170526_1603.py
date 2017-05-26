# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercaderias', '0002_auto_20170526_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriamercaderia',
            name='subcategoria',
            field=models.OneToOneField(to='mercaderias.CategoriaMercaderia', blank=True),
        ),
    ]
