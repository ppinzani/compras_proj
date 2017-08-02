from django.db import models

from shortuuidfield import ShortUUIDField
from proveedores.models import Proveedor


# Create your models here.
class CategoriaMercaderia(models.Model):
    nombre = models.CharField(max_length=80)
    padre = models.OneToOneField('self',
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)

    class Meta:
        verbose_name = "Categoria De Mercaderia"
        verbose_name_plural = "Categorias de Mercaderia"

    def __str__(self):
        return u"%s" % self.nombre

    #@models.permalink
    #def get_absolute_url(self):
    #    return 'mercaderias:detalle', [self.id]

    @models.permalink
    def get_update_url(self):
        return 'mercaderias:editar_categoria', [self.id]

    @models.permalink
    def get_delete_url(self):
        return 'mercaderias:borrar_categoria', [self.id]


class Mercaderia(models.Model):
    #sku = FIXME
    descripcion = models.CharField(max_length=100, blank=True)
    categorias = models.ManyToManyField(CategoriaMercaderia, blank=True)
    iva = models.DecimalField(max_digits=4, decimal_places=2, default=21.0)
    #Fecha ultima actualizacion
    #Activa o no
    #Stock minimo

    class Meta:
        verbose_name = "Mercaderia"
        verbose_name_plural = "Mercaderias"

    def __str__(self):
        return u"%s" % self.descripcion

    #@models.permalink
    #def get_absolute_url(self):
    #    return 'mercaderias:detalle', [self.id]

    @models.permalink
    def get_update_url(self):
        return 'mercaderias:editar', [self.id]

    @models.permalink
    def get_delete_url(self):
        return 'mercaderias:borrar', [self.id]


class MercaderiaProveedor(models.Model):
    mercaderia = models.ForeignKey(Mercaderia)
    proveedor = models.ForeignKey(Proveedor)
    ultimo_precio = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    #Ver de agregar precio de lista y precio de contado
    #margen de ganancia FIXME

    class Meta:
        verbose_name = 'MercaderiaProveedor'
        verbose_name_plural = "MercaderiasProveedores"

    def __str__(self):
        return "%s(%s)" % (self.mercaderia, self.proveedor)
