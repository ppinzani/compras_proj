# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mercaderia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('uuid', shortuuidfield.fields.ShortUUIDField(editable=False, max_length=22, unique=True, blank=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Mercaderia',
                'verbose_name_plural': 'Mercaderias',
            },
        ),
    ]
