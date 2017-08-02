# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercaderias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mercaderia',
            old_name='categoria',
            new_name='categorias',
        ),
        migrations.AddField(
            model_name='mercaderia',
            name='iva',
            field=models.DecimalField(max_digits=4, decimal_places=2, default=21.0),
        ),
    ]
