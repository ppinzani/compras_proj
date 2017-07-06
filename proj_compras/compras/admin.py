from django.contrib import admin
from .models import SolicitudDeCompra, Cotizacion, OrdenDeCompra
from .models import PagoDeCompra, FacturaDeCompra


# Register your models here.
admin.site.register(SolicitudDeCompra)
admin.site.register(Cotizacion)
admin.site.register(OrdenDeCompra)
admin.site.register(PagoDeCompra)
admin.site.register(FacturaDeCompra)
