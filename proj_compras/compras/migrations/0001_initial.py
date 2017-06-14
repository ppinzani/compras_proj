# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mercaderias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleSolicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('mercaderia', models.ForeignKey(to='mercaderias.Mercaderia')),
            ],
            options={
                'verbose_name': 'DetalleSolicitud',
                'verbose_name_plural': 'DetallesSolicitud',
            },
        ),
        migrations.CreateModel(
            name='SolicitudDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('estado', models.CharField(choices=[('A', 'Aprobada'), ('P', 'Aprobacion Pendiente')], max_length=5, default='P')),
                ('fecha_generada', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('observaciones', models.TextField(null=True, blank=True)),
                ('aprobada_por', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, related_name='aprobada_por')),
                ('generada_por', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, related_name='generada_por')),
            ],
            options={
                'verbose_name': 'SolicitudDeCompra',
                'verbose_name_plural': 'SolicitudesDeCompra',
            },
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='solicitud',
            field=models.ForeignKey(to='compras.SolicitudDeCompra'),
        ),
    ]
