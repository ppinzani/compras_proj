# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercaderias', '0006_remove_mercaderia_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriamercaderia',
            old_name='subcategoria',
            new_name='padre',
        ),
    ]
