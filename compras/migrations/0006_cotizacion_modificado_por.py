# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compras', '0005_auto_20170618_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='modificado_por',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='modificado_por', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
    ]
