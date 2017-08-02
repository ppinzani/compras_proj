# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0009_auto_20170626_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagodecompra',
            name='estado',
            field=models.CharField(choices=[('Pa', 'Pagado'), ('Pe', 'Pendiente')], null=True, max_length=5, blank=True, default='Pe'),
        ),
        migrations.AlterField(
            model_name='pagodecompra',
            name='fecha_de_pago',
            field=models.DateField(blank=True, null=True),
        ),
    ]
