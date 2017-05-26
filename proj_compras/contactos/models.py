from django.db import models

from shortuuidfield import ShortUUIDField

from proveedores.models import Proveedor


# Create your models here.
class Contacto(models.Model):
    uuid = ShortUUIDField(unique=True)
    proveedor = models.ForeignKey(Proveedor,
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  null=True
                                  )
    nombre = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    #FIXME Cantidad dinamica de telofonos?
    telefono = models.CharField(max_length=40, blank=True)
    #telefono_2 = models.CharField(max_length=40, blank=True)
    direccion = models.CharField(max_length=80, blank=True)
    #FIXME Se podria agregar una tabla direccion con ciudad, provincia, etc
    #direccion_2 = models.CharField(max_length=80, blank=True)
    pagina_web = models.URLField(blank=True)
    detalles = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'contactos'

    @models.permalink
    def get_absolute_url(self):
        return 'contactos:detalle', [self.uuid]

    @models.permalink
    def get_update_url(self):
        return 'contactos:editar', [self.uuid]

    @models.permalink
    def get_delete_url(self):
        return 'contactos:borrar', [self.id]
