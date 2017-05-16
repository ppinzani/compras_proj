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

    def __unicode__(self):
        return u"%s" % self.nombre_fiscal

    @models.permalink
    def get_absolute_url(self):
        return 'proveedores:detalle', [self.uuid]

    @models.permalink
    def get_update_url(self):
        return 'proveedores:editar', [self.uuid]

    @models.permalink
    def get_delete_url(self):
        return 'proveedores:borrar', [self.uuid]


class ContactoProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor,
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  null=True
                                  )
    nombre = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    telefono_1 = models.CharField(max_length=40, blank=True)
    telefono_2 = models.CharField(max_length=40, blank=True)
    direccion_1 = models.CharField(max_length=80, blank=True)
    direccion_2 = models.CharField(max_length=80, blank=True)
    pagina_web = models.URLField(blank=True)
    detalles = models.TextField(blank=True)
