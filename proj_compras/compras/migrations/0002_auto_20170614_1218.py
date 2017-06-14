# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicituddecompra',
            options={'verbose_name_plural': 'SolicitudesDeCompra', 'permissions': (('puede_aprobar_solicitud', 'Puede aprobar las solicitudes pendientes'),), 'verbose_name': 'SolicitudDeCompra'},
        ),
    ]
