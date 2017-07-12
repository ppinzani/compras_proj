# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0017_auto_20170704_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagodecompra',
            name='foto',
            field=models.ImageField(upload_to='comprobantes_de_pago', blank=True),
        ),
        migrations.AlterField(
            model_name='pagodecompra',
            name='estado',
            field=models.CharField(max_length=5, null=True, default='Pe', blank=True, choices=[('Pa', 'Pagado'), ('Pc', 'Pagado, Comprobante Enviado'), ('Pe', 'Pendiente')]),
        ),
    ]
