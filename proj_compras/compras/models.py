from django.db import models
from django.conf import settings

from mercaderias.models import Mercaderia
from proj_compras.constants import ESTADO_SOLICITUD_CHOICES
from proj_compras.constants import PENDIENTE


# Create your models here.
class SolicitudDeCompra(models.Model):

    estado = models.CharField(max_length=5,
                              choices=ESTADO_SOLICITUD_CHOICES,
                              default=PENDIENTE)
    fecha_generada = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    generada_por = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET_NULL,
                                     blank=True,
                                     null=True,
                                     related_name='generada_por')
    aprobada_por = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET_NULL,
                                     blank=True,
                                     null=True,
                                     related_name='aprobada_por')
    observaciones = models.TextField(blank=True,
                                     null=True)

    class Meta:
        verbose_name = "SolicitudDeCompra"
        verbose_name_plural = "SolicitudesDeCompra"
        permissions = (
            ("puede_aprobar_solicitud",
             "Puede aprobar las solicitudes pendientes"),
        )

    def __str__(self):
        return self.id

    @models.permalink
    def get_absolute_url(self):
        return 'compras:detalle_solicitud', [self.id]

    @models.permalink
    def get_update_url(self):
        return 'compras:editar_solicitud', [self.id]

    @models.permalink
    def get_delete_url(self):
        return 'compras:borrar_solicitud', [self.id]


class DetalleSolicitud(models.Model):

    cantidad = models.PositiveIntegerField()
    mercaderia = models.ForeignKey(Mercaderia)
    solicitud = models.ForeignKey(SolicitudDeCompra,
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name = "DetalleSolicitud"
        verbose_name_plural = "DetallesSolicitud"

    def __str__(self):
        return self.id