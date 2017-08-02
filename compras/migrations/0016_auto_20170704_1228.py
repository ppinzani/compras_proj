# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0015_auto_20170704_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendecompra',
            name='forma_de_pago',
            field=models.CharField(choices=[('E', 'Contado Efectivo'), ('C', 'En cuotas')], max_length=5, null=True),
        ),
    ]
