from django.db import models
from django.conf import settings
from django.utils.timezone import now
from decimal import Decimal

from mercaderias.models import Mercaderia
from proveedores.models import Proveedor
from proj_compras.constants import ESTADO_SOLICITUD_CHOICES, SOLICITUD_PENDIENTE
from proj_compras.constants import ESTADO_COTIZACION_CHOICES, COTIZACION_PENDIENTE
from proj_compras.constants import ESTADO_PAGO_CHOICES, PAGO_PENDIENTE
from proj_compras.constants import FORMA_DE_PAGO_CHOICES, CONTADO
from proj_compras.constants import TIPO_FACTURA_CHOICES, FACTURA_A


# Create your models here.
class SolicitudDeCompra(models.Model):

    estado = models.CharField(max_length=5,
                              choices=ESTADO_SOLICITUD_CHOICES,
                              default=SOLICITUD_PENDIENTE)
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
        return "SolicitudDeCompra:%s" % self.id

    @models.permalink
    def get_absolute_url(self):
        return 'compras:detalle_solicitud', [self.id]

    @models.permalink
    def get_update_url(self):
        return 'compras:editar_solicitud', [self.id]

    @models.permalink
    def get_delete_url(self):
        return 'compras:borrar_solicitud', [self.id]

    @models.permalink
    def get_aprobar_url(self):
        return 'compras:aprobar_solicitud', [self.id]


class DetalleSolicitud(models.Model):
    cantidad = models.PositiveIntegerField()
    mercaderia = models.ForeignKey(Mercaderia)
    solicitud = models.ForeignKey(SolicitudDeCompra,
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name = "DetalleSolicitud"
        verbose_name_plural = "DetallesSolicitud"

    def __str__(self):
        return "DetalleSolicitud:%s" % self.id


class Cotizacion(models.Model):
    fecha_generada = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=5,
                              choices=ESTADO_COTIZACION_CHOICES,
                              default=COTIZACION_PENDIENTE)
    modificado_por = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL,
                                       blank=True,
                                       null=True,
                                       related_name='modificado_por')
    proveedor = models.ForeignKey(Proveedor,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True)
    solicitud = models.ForeignKey(SolicitudDeCompra,
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True)
    descuento = models.PositiveIntegerField(blank=True, null=True, default=0)
    iva = models.PositiveIntegerField(default=21)

    def get_subtotal(self):
        detalles = DetalleCotizacion.objects.filter(cotizacion=self)
        total = 0
        for d in detalles:
            total = total + d.get_subtotal()

        return total

    def get_calculo_iva(self):
        return round(self.get_subtotal() * Decimal(
            (1.0 - self.descuento / 100.0) * (self.iva / 100.0)), 2)

    def get_calculo_descuento(self):
        return round(self.get_subtotal() * Decimal(self.descuento / 100.0), 2)

    def get_total(self):
        return round(self.get_subtotal() * Decimal(
            (1.0 - self.descuento / 100.0) * (1.0 + self.iva / 100.0)), 2)

    class Meta:
        verbose_name = "Cotizacion"
        verbose_name_plural = "Cotizaciones"
        permissions = (
            ("puede_aprobar_orden_de_compra",
             "Puede aprobar las cotizaciones pendientes"),
        )

    @models.permalink
    def get_absolute_url(self):
        return 'compras:detalle_cotizacion', [self.id]

    @models.permalink
    def get_update_url(self):
        return 'compras:editar_cotizacion', [self.id]

    @models.permalink
    def get_delete_url(self):
        return 'compras:borrar_cotizacion', [self.id]

    @models.permalink
    def get_aprobar_url(self):
        return 'compras:aprobar_cotizacion', [self.id]

    @models.permalink
    def get_rechazar_url(self):
        return 'compras:rechazar_cotizacion', [self.id]

    def __str__(self):
        return "Cotizacion: %s" % self.id


class DetalleCotizacion(models.Model):
    cantidad = models.PositiveIntegerField()
    mercaderia = models.ForeignKey(Mercaderia)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    cotizacion = models.ForeignKey(Cotizacion,
                                   on_delete=models.CASCADE)

    def get_subtotal(self):
        return self.cantidad * self.precio

    class Meta:
        verbose_name = "DetalleCotizacion"
        verbose_name_plural = "DetallesCotizacion"

    def __str__(self):
        return "%s" % self.id


class OrdenDeCompra(models.Model):
    numero = models.PositiveIntegerField(unique=True, default=0)
    cotizacion = models.ForeignKey(Cotizacion)
    forma_de_pago = models.CharField(
        max_length=5,
        choices=FORMA_DE_PAGO_CHOICES,
        null=True  # Fixme cambiar por blank
    )
    cuotas = models.PositiveIntegerField(blank=True, default=1)
    #fecha_generada
    #fecha_ultima_modificacion
    #fecha_de_entrega

    class Meta:
        verbose_name = "OrdenDeCompra"
        verbose_name_plural = "OrdenesDeCompra"

    def __str__(self):
        return "Orden de Compra nro: %s" % self.numero

    def get_subtotal(self):
        return self.cotizacion.get_subtotal()

    def get_calculo_iva(self):
        return self.cotizacion.get_calculo_iva()

    def get_calculo_descuento(self):
        return self.cotizacion.get_calculo_descuento()

    def get_total(self):
        return self.cotizacion.get_total()

    @models.permalink
    def get_absolute_url(self):
        return 'compras:detalle_orden', [self.id]

    @models.permalink
    def get_update_url(self):
        return 'compras:editar_orden', [self.id]

    @models.permalink
    def get_delete_url(self):
        return 'compras:borrar_orden', [self.id]


class FacturaDeCompra(models.Model):
    numero = models.PositiveIntegerField()
    fecha = models.DateField(blank=True)
    importe = models.DecimalField(max_digits=15, decimal_places=2)
    foto = models.ImageField(upload_to='facturas_de_compra', blank=True)
    tipo = models.CharField(
        max_length=5,
        choices=TIPO_FACTURA_CHOICES,
        default=FACTURA_A
    )
    orden = models.OneToOneField(
        OrdenDeCompra,
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = "FacturaDeCompra"
        verbose_name_plural = "FacturasDeCompra"

    def __str__(self):
        return "Factura nro: %s" % self.numero

    def get_proveedor(self):
        return self.orden.cotizacion.proveedor

    def get_detalles(self):
        detalles = DetalleCotizacion.objects.filter(
            cotizacion=self.orden.cotizacion
        )
        return detalles

    def get_subtotal(self):
        return self.orden.get_subtotal()

    def get_calculo_iva(self):
        return self.orden.get_calculo_iva()

    def get_calculo_descuento(self):
        return self.orden.get_calculo_descuento()

    def get_total(self):
        return self.orden.get_total()

    @models.permalink
    def get_absolute_url(self):
        return 'compras:detalle_factura', [self.id]

    @models.permalink
    def get_update_url(self):
        return 'compras:editar_factura', [self.id]

    @models.permalink
    def get_delete_url(self):
        return 'compras:borrar_factura', [self.id]


#class DetalleOrdenCompra(models.Model):
#    cantidad = models.PositiveIntegerField()
#    mercaderia = models.ForeignKey(Mercaderia)
#    precio = models.DecimalField(max_digits=15, decimal_places=3)
#    orden = models.ForeignKey(Cotizacion,
#                              on_delete=models.CASCADE)
#
#    def get_subtotal(self):
#        return self.cantidad * self.precio
#
#    class Meta:
#        verbose_name = "DetalleOrdenDeCompra"
#        verbose_name_plural = "DetallesOrdenDeCompra"
#
#    def __str__(self):
#        pass


class PagoDeCompra(models.Model):
    fecha_de_pago = models.DateField(blank=True, null=True)
    orden = models.ForeignKey(OrdenDeCompra)
    importe = models.DecimalField(max_digits=15, decimal_places=2)
    estado = models.CharField(max_length=5,
                              choices=ESTADO_PAGO_CHOICES,
                              null=True,
                              blank=True,
                              default=PAGO_PENDIENTE)
    foto = models.ImageField(upload_to='comprobantes_de_pago', blank=True)

    class Meta:
        verbose_name = "PagoDeCompra"
        verbose_name_plural = "PagosDeCompra"

    def __str__(self):
        return "PagosDeCompra:%s" % self.id
