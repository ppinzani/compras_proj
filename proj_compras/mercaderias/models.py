from django.db import models

from shortuuidfield import ShortUUIDField


# Create your models here.
class CategoriaMercaderia(models.Model):
    nombre = models.CharField(max_length=80)
    subcategoria = models.OneToOneField('self',
                                        on_delete=models.CASCADE,
                                        blank=True,
                                        null=True)

    class Meta:
        verbose_name = "Categoria De Mercaderia"
        verbose_name_plural = "Categorias de Mercaderia"


class Mercaderia(models.Model):
    uuid = ShortUUIDField(unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    categoria = models.ManyToManyField(CategoriaMercaderia,
                                       blank=True)

    class Meta:
        verbose_name = "Mercaderia"
        verbose_name_plural = "Mercaderias"

    def __unicode__(self):
        return u"%s" % self.nombre

    @models.permalink
    def get_absolute_url(self):
        return 'mercaderias:detalle', [self.uuid]

    @models.permalink
    def get_update_url(self):
        return 'mercaderias:editar', [self.uuid]

    @models.permalink
    def get_delete_url(self):
        return 'mercaderias:borrar', [self.id]
