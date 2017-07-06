# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0016_auto_20170704_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturadecompra',
            name='fecha',
            field=models.DateField(blank=True),
        ),
    ]
