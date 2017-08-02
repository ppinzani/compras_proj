# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0011_auto_20170629_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='iva',
            field=models.PositiveIntegerField(default=21),
        ),
    ]
