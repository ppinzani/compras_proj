from django.db import models
from django.utils.timezone import now

from shortuuidfield import ShortUUIDField


# Create your models here.
class ContactoProveedor(models.Model):
    nombre = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    telefono_1 = models.CharField(max_length=40, blank=True)
    telefono_2 = models.CharField(max_length=40, blank=True)
    direccion_1 = models.CharField(max_length=80, blank=True)
    direccion_2 = models.CharField(max_length=80, blank=True)
    url = models.URLField(blank=True)
    detalles = models.TextField(blank=True)


class Proveedor(models.Model):
    CONS_FINAL = 'CF'
    RESPONSABLE_INSCRIPTO = 'RI'
    RESPONSABLE_NO_INSCRIPTO = 'RNI'
    MONOTRIBUTO = 'MONO'
    OTRO = 'OTRO'
    condicion_iva_choices = (
        (CONS_FINAL, 'Consumidor Final'),
        (RESPONSABLE_INSCRIPTO, 'IVA Responsable Inscripto'),
        (RESPONSABLE_NO_INSCRIPTO, 'IVA Responsable No Inscripto'),
        (MONOTRIBUTO, 'Monotributo'),
        (OTRO, 'Otro'),
    )

    uuid = ShortUUIDField(unique=True)
    nombre_fiscal = models.CharField(max_length=100)
    nombre_fantasia = models.CharField(max_length=100, blank=True)
    fecha_alta = models.DateField(default=now, blank=True)
    cuit = models.CharField(max_length=25, blank=True)
    margen_ganancia = models.SmallIntegerField(blank=True, null=True)
    condicion_iva = models.CharField(max_length=5,
                                     choices=condicion_iva_choices,
                                     default=RESPONSABLE_INSCRIPTO)
    contacto = models.ForeignKey(ContactoProveedor,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True
                                 )

    class Meta:
        verbose_name_plural = 'proveedores'

    def __unicode__(self):
        return u"%s" % self.nombre_fiscal
