# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercaderias', '0004_auto_20170526_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercaderia',
            name='categoria',
            field=models.ManyToManyField(to='mercaderias.CategoriaMercaderia', blank=True),
        ),
    ]
