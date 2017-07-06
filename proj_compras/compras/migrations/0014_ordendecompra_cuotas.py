# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0013_auto_20170630_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordendecompra',
            name='cuotas',
            field=models.PositiveIntegerField(default=1, blank=True),
        ),
    ]
