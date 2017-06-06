# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercaderias', '0007_auto_20170601_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mercaderia',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='mercaderia',
            name='descripcion',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
