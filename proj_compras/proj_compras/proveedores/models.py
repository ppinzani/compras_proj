from django.db import models
from django.utils.timezone import now

from shortuuidfield import ShortUUIDField
from proj_compras.constants import CONDICION_IVA_CHOICES
from proj_compras.constants import NO_ESPECIFICA


# Create your models here.
class Proveedor(models.Model):
    uuid = ShortUUIDField(unique=True)
    nombre_fiscal = models.CharField(max_length=100)
    nombre_fantasia = models.CharField(max_length=100, blank=True)
    fecha_alta = models.DateField(default=now(), blank=True)
    cuit = models.CharField(max_length=25, blank=True)
    margen_ganancia = models.SmallIntegerField(blank=True, null=True)
    condicion_iva = models.CharField(max_length=5,
                                     choices=CONDICION_IVA_CHOICES,
                                     default=NO_ESPECIFICA)

    class Meta:
        verbose_name_plural = 'proveedores'

    def display_name(self):
        if self.nombre_fantasia:
            return self.nombre_fantasia
        return self.nombre_fiscal

    def __unicode__(self):
        return u"%s" % self.display_name

    @models.permalink
    def get_absolute_url(self):
        return 'proveedores:detalle', [self.uuid]

    @models.permalink
    def get_update_url(self):
        return 'proveedores:editar', [self.uuid]

    @models.permalink
    def get_delete_url(self):
        return 'proveedores:borrar', [self.uuid]
