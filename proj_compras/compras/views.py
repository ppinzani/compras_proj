from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.db import IntegrityError, transaction
from django.contrib import messages
from django.views.generic import ListView, DeleteView, RedirectView
from django.views.generic import UpdateView, DetailView
from django.views.generic.edit import FormView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from datetime import date


from proj_compras.constants import SOLICITUD_APROBADA
from proj_compras.constants import COTIZACION_APROBADA, COTIZACION_RECHAZADA
from .models import SolicitudDeCompra, DetalleSolicitud
from .models import Cotizacion, DetalleCotizacion
from .models import OrdenDeCompra, PagoDeCompra, FacturaDeCompra
from .forms import DetalleSolicitudForm, SolicitudDeCompraForm
from .forms import BaseSolicitudFormSet, BaseCotizacionFormSet
from .forms import CotizacionForm, DetalleCotizacionForm
from .forms import OrdenDeCompraForm, FacturaDeCompraForm
from .forms import PagoDeCompraForm, BasePagoFormSet


class SolicitudDeCompraList(LoginRequiredMixin, ListView):
    model = SolicitudDeCompra
    template_name = 'compras/solicitudes_lista.html'
    #This name can then be later used in templates.
    context_object_name = 'solicitudes'
    redirect_field_name = '/login/'


@login_required()
def detalle_solicitud_de_compra(request, pk):
    solicitud = SolicitudDeCompra.objects.get(pk=pk)
    detalles = DetalleSolicitud.objects.filter(solicitud=solicitud)

    variables = {
        'solicitud': solicitud,
        'detalles': detalles
    }

    return render(request, 'compras/detalle_solicitud.html', variables)


class BorrarSolicitudDeCompra(LoginRequiredMixin, PermissionRequiredMixin,
                              DeleteView):
    model = SolicitudDeCompra
    template_name = 'compras/eliminar_solicitud.html'
    permission_required = 'compras.delete_solicituddecompras'
    raise_exception = True
    success_url = '/compras/solicitudes/'


class AprobarSolicitudDeCompra(LoginRequiredMixin, PermissionRequiredMixin,
                               RedirectView):
    permission_required = 'compras.puede_aprobar_solicitud'
    raise_exception = True
    permanent = False
    url = "/compras/solicitudes/"

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(AprobarSolicitudDeCompra, self).dispatch(*args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        solicitud = get_object_or_404(SolicitudDeCompra, pk=kwargs['pk'])
        solicitud.estado = SOLICITUD_APROBADA
        solicitud.aprobada_por = self.request.user
        solicitud.save()
        return super(AprobarSolicitudDeCompra, self).get_redirect_url(*args,
                                                                      **kwargs)


@login_required()
def solicitud_de_compra_cru(request, pk=None):

    DetalleFormSet = formset_factory(DetalleSolicitudForm,
                                     formset=BaseSolicitudFormSet)

    if pk:
        if not request.user.has_perm('compras.change_solicituddecompra'):
            return HttpResponseForbidden()
        solicitud = get_object_or_404(SolicitudDeCompra, pk=pk)
    else:
        if not request.user.has_perm('compras.add_solicituddecompra'):
            return HttpResponseForbidden()
        solicitud = SolicitudDeCompra()

    detalles = DetalleSolicitud.objects.filter(solicitud=solicitud)

    datos_detalle = [{'cantidad': d.cantidad, 'mercaderia': d.mercaderia}
                     for d in detalles]

    if request.POST:
        solicitud_form = SolicitudDeCompraForm(request.POST,
                                               instance=solicitud)
        detalle_formset = DetalleFormSet(request.POST)

        if solicitud_form.is_valid() and detalle_formset.is_valid():
            #Guardo los detalles de la solicitud
            solicitud.generada_por = solicitud_form.cleaned_data['generada_por']
            solicitud.estado = solicitud_form.cleaned_data['estado']
            if solicitud_form.cleaned_data['estado'] == SOLICITUD_APROBADA:
                if not request.user.has_perm('compras.puede_aprobar_solicitud'):
                    return HttpResponseForbidden()
                solicitud.aprobada_por = request.user
            else:
                solicitud.aprobada_por = None
            solicitud.save()

            nuevos_detalles = []

            for detalle_form in detalle_formset:
                cantidad = detalle_form.cleaned_data.get('cantidad')
                mercaderia = detalle_form.cleaned_data.get('mercaderia')

                if cantidad and mercaderia:
                    nuevos_detalles.append(DetalleSolicitud(cantidad=cantidad,
                                                            mercaderia=mercaderia,
                                                            solicitud=solicitud))

            try:
                with transaction.atomic():
                    #Reemplazo los viejos con los nuevo
                    DetalleSolicitud.objects.filter(solicitud=solicitud).delete()
                    DetalleSolicitud.objects.bulk_create(nuevos_detalles)
                    return redirect(reverse('compras:detalle_solicitud',
                                            args=(solicitud.id,)))
            except IntegrityError:
                messages.error(request, 'Error grabando la solicitud!')

    else:
        if pk:
            solicitud_form = SolicitudDeCompraForm(instance=solicitud)
        else:
            solicitud_form = SolicitudDeCompraForm(
                initial={'generada_por': request.user.pk},
                instance=solicitud
            )

        detalle_formset = DetalleFormSet(initial=datos_detalle)

    variables = {
        'solicitud_form': solicitud_form,
        'solicitud': solicitud,
        'detalle_formset': detalle_formset,
    }

    template = 'compras/create_update_solicitud.html'

    return render(request, template, variables)


class CotizacionesList(LoginRequiredMixin, ListView):
    model = Cotizacion
    template_name = 'compras/cotizaciones_lista.html'
    #This name can then be later used in templates.
    context_object_name = 'cotizaciones'
    redirect_field_name = '/login/'


@login_required()
def detalle_cotizacion(request, pk):
    cotizacion = Cotizacion.objects.get(pk=pk)
    detalles = DetalleCotizacion.objects.filter(cotizacion=cotizacion)

    variables = {
        'cotizacion': cotizacion,
        'detalles': detalles
    }

    return render(request, 'compras/detalle_cotizacion.html', variables)


class BorrarCotizacion(LoginRequiredMixin, PermissionRequiredMixin,
                       DeleteView):
    model = Cotizacion
    template_name = 'compras/eliminar_cotizacion.html'
    permission_required = 'compras.delete_cotizacion'
    raise_exception = True
    success_url = '/compras/cotizaciones/'


class AprobarCotizacion(LoginRequiredMixin, PermissionRequiredMixin,
                        RedirectView):
    permission_required = 'compras.puede_aprobar_cotizacion'
    raise_exception = True
    permanent = False
    url = "/compras/cotizaciones/"

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(AprobarCotizacion, self).dispatch(*args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        cotizacion = get_object_or_404(Cotizacion, pk=kwargs['pk'])
        cotizacion.estado = COTIZACION_APROBADA
        cotizacion.modificado_por = self.request.user
        cotizacion.save()
        return super(AprobarCotizacion, self).get_redirect_url(*args, **kwargs)


class RechazarCotizacion(LoginRequiredMixin, PermissionRequiredMixin,
                         RedirectView):
    permission_required = 'compras.puede_aprobar_cotizacion'
    raise_exception = True
    permanent = False
    url = "/compras/cotizaciones/"

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(RechazarCotizacion, self).dispatch(*args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        cotizacion = get_object_or_404(Cotizacion, pk=kwargs['pk'])
        cotizacion.estado = COTIZACION_RECHAZADA
        cotizacion.modificado_por = self.request.user
        cotizacion.save()
        return super(RechazarCotizacion, self).get_redirect_url(*args, **kwargs)


@login_required()
def cotizacion_cru(request, pk=None):

    DetalleFormSet = formset_factory(DetalleCotizacionForm,
                                     formset=BaseCotizacionFormSet,
                                     extra=0)

    solicitud = None

    if pk:
        if not request.user.has_perm('compras.change_cotizacion'):
            return HttpResponseForbidden()
        cotizacion = get_object_or_404(Cotizacion, pk=pk)
    else:
        if not request.user.has_perm('compras.add_cotizacion'):
            return HttpResponseForbidden()
        cotizacion = Cotizacion()

    # Uso para obtener la solicitud si es un parametro en la url
    if request.GET.get('solicitud', ''):
        solicitud = SolicitudDeCompra.objects.get(id=request.GET.get('solicitud', ''))
        cotizacion.solicitud = solicitud

    # Armo los detalles dependiendo de si es una nueva cotizacion o
    # solo quiero editar
    if solicitud:
        ds = DetalleSolicitud.objects.filter(solicitud=solicitud)
        datos_detalle = [{'cantidad': d.cantidad,
                          'mercaderia': d.mercaderia}
                         for d in ds]
    else:
        detalles = DetalleCotizacion.objects.filter(cotizacion=cotizacion)
        datos_detalle = [{'cantidad': d.cantidad,
                          'mercaderia': d.mercaderia,
                          'precio': d.precio}
                         for d in detalles]

    if request.POST:
        cotizacion_form = CotizacionForm(request.POST, instance=cotizacion)
        detalle_formset = DetalleFormSet(request.POST)

        if cotizacion_form.is_valid() and detalle_formset.is_valid():
            #Guardo los detalles de la solicitud

            cotizacion.proveedor = cotizacion_form.cleaned_data['proveedor']
            if cotizacion_form.cleaned_data['estado'] != cotizacion.estado:
                if not request.user.has_perm('compras.puede_aprobar_cotizacion'):
                    return HttpResponseForbidden()
                cotizacion.estado = cotizacion_form.cleaned_data['estado']
                cotizacion.modificado_por = request.user
            cotizacion.save()

            nuevos_detalles = []

            for detalle_form in detalle_formset:
                cantidad = detalle_form.cleaned_data.get('cantidad')
                mercaderia = detalle_form.cleaned_data.get('mercaderia')
                precio = detalle_form.cleaned_data.get('precio')

                if cantidad and mercaderia and precio:
                    nuevos_detalles.append(
                        DetalleCotizacion(
                            cantidad=cantidad,
                            mercaderia=mercaderia,
                            precio=precio,
                            cotizacion=cotizacion
                        )
                    )

            try:
                with transaction.atomic():
                    #Reemplazo los viejos con los nuevo
                    DetalleCotizacion.objects.filter(cotizacion=cotizacion).delete()
                    DetalleCotizacion.objects.bulk_create(nuevos_detalles)
                    # And notify our users that it worked
                    return redirect(reverse('compras:detalle_cotizacion',
                                            args=(cotizacion.id,)))
            except IntegrityError:
                messages.error(request, 'Error grabando la cotizacion!')
    else:
        cotizacion_form = CotizacionForm(instance=cotizacion)
        detalle_formset = DetalleFormSet(initial=datos_detalle)

    variables = {
        'cotizacion_form': cotizacion_form,
        'cotizacion': cotizacion,
        'detalle_formset': detalle_formset,
    }

    template = 'compras/create_update_cotizacion.html'

    return render(request, template, variables)


class OrdenesList(LoginRequiredMixin, ListView):
    model = OrdenDeCompra
    template_name = 'compras/ordenes_lista.html'
    #This name can then be later used in templates.
    context_object_name = 'ordenes'
    redirect_field_name = '/login/'


@login_required()
def detalle_orden(request, pk):
    orden = OrdenDeCompra.objects.get(pk=pk)
    detalles = DetalleCotizacion.objects.filter(cotizacion=orden.cotizacion)
    pagos = PagoDeCompra.objects.filter(orden=orden)

    variables = {
        'orden': orden,
        'detalles': detalles,
        'pagos': pagos,
    }

    return render(request, 'compras/detalle_orden.html', variables)


class BorrarOrdenDeCompra(LoginRequiredMixin, PermissionRequiredMixin,
                          DeleteView):
    model = OrdenDeCompra
    template_name = 'compras/eliminar_orden.html'
    permission_required = 'compras.delete_ordendecompra'
    raise_exception = True
    success_url = '/compras/ordenes/'


@login_required()
def orden_de_compra_cru(request, pk=None):
    cotizacion = None
    pagos_formset = None
    PagoFormSet = formset_factory(
        PagoDeCompraForm,
        formset=BasePagoFormSet,
        extra=0
    )

    if pk:
        if not request.user.has_perm('compras.change_ordendecompra'):
            return HttpResponseForbidden()
        orden = get_object_or_404(OrdenDeCompra, pk=pk)
    else:
        if not request.user.has_perm('compras.add_ordendecompra'):
            return HttpResponseForbidden()
        orden = OrdenDeCompra()

    # Uso para obtener la solicitud si es un parametro en la url
    if request.GET.get('cotizacion', ''):
        cotizacion = Cotizacion.objects.get(
            id=request.GET.get('cotizacion', '')
        )
        orden.cotizacion = cotizacion

    pagos = PagoDeCompra.objects.filter(orden=orden)
    datos_pagos = [{'fecha_de_pago': p.fecha_de_pago,
                    'importe': p.importe,
                    'estado': p.estado} for p in pagos]

    if request.POST:
        orden_form = OrdenDeCompraForm(request.POST, instance=orden)
        pagos_formset = PagoFormSet(request.POST)
        errors = False

        if orden_form.is_valid() and pagos_formset.is_valid():
            #Guardo los detalles de la orden
            orden.numero = orden_form.cleaned_data['numero']
            orden.forma_de_pago = orden_form.cleaned_data['forma_de_pago']
            if not orden_form.cleaned_data['cuotas']:
                orden.cuotas = 1
            else:
                orden.cuotas = orden_form.cleaned_data['cuotas']
            orden.save()

            nuevos_pagos = []
            total_pagos = 0

            for pago_form in pagos_formset:
                fecha = pago_form.cleaned_data.get('fecha_de_pago')
                importe = pago_form.cleaned_data.get('importe')

                if fecha and importe:
                    nuevos_pagos.append(
                        PagoDeCompra(
                            fecha_de_pago=fecha,
                            orden=orden,
                            importe=importe
                        )
                    )
                    total_pagos = total_pagos + importe

            if total_pagos != orden.cotizacion.get_total():
                messages.error(
                    request,
                    'Error grabando los pagos: El total de los pagos (%s) \
                    no coincide con el de la orden(%s)'
                    % (str(total_pagos), str(orden.cotizacion.get_total()))
                )
                errors = True

            if len(nuevos_pagos) >= 1:
                try:
                    with transaction.atomic():
                        PagoDeCompra.objects.filter(orden=orden).delete()
                        PagoDeCompra.objects.bulk_create(nuevos_pagos)

                except IntegrityError:
                    messages.error(request, 'Error grabando los pagos!')

            if not errors:
                return redirect('/compras/ordenes/')
        else:
            messages.error(request, 'Error grabando los pagos!')

    else:
        orden_form = OrdenDeCompraForm(instance=orden)
        pagos_formset = PagoFormSet(initial=datos_pagos)

    detalles = DetalleCotizacion.objects.filter(cotizacion=orden.cotizacion)

    template = 'compras/create_update_orden.html'

    #Si quiero agregar pagos
    if request.GET.get('cuotas', ''):
            cantidad_pagos = int(request.GET.get('cuotas', ''))
            PagoFormSet = formset_factory(
                PagoDeCompraForm,
                formset=BasePagoFormSet,
                extra=cantidad_pagos
            )
            pagos_formset = PagoFormSet()
            template = 'compras/pagos_form.html'

    variables = {
        'orden_form': orden_form,
        'orden': orden,
        'detalles': detalles,
        'pagos_formset': pagos_formset,
    }

    return render(request, template, variables)


class CrearFactura(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    form_class = FacturaDeCompraForm
    template_name = 'compras/create_update_factura.html'
    success_url = '/compras/facturas'
    permission_required = 'compras.add_facturadecompra'
    raise_exception = True

    def form_valid(self, form):
        orden = OrdenDeCompra.objects.get(pk=self.request.GET.get('orden', ''))
        form.instance.orden = orden
        form.instance.save()
        return super(CrearFactura, self).form_valid(form)

    def get_initial(self):
        initial = super(CrearFactura, self).get_initial()
        orden = OrdenDeCompra.objects.get(pk=self.request.GET.get('orden', ''))
        initial['importe'] = orden.get_total()

        return initial


class FacturasList(LoginRequiredMixin, ListView):
    model = FacturaDeCompra
    template_name = 'compras/facturas_lista.html'
    #This name can then be later used in templates.
    context_object_name = 'facturas'
    redirect_field_name = '/login/'


class DetalleFactura(LoginRequiredMixin, DetailView):
    model = FacturaDeCompra
    template_name = 'compras/detalle_factura.html'
    context_object_name = 'factura'
    redirect_field_name = '/login/'


class ActualizarFactura(LoginRequiredMixin, PermissionRequiredMixin,
                        UpdateView):
    form_class = FacturaDeCompraForm
    template_name = 'compras/create_update_factura.html'
    model = FacturaDeCompra
    permission_required = 'compras.change_facturadecompra'
    raise_exception = True
    redirect_field_name = '/login/'

    def get_success_url(self):
        return reverse('compras:detalle_factura', kwargs={'pk': self.pk})


class BorrarFactura(LoginRequiredMixin, PermissionRequiredMixin,
                    DetailView):
    template_name = 'compras/eliminar_factura.html'
    model = FacturaDeCompra
    success_url = '/compras/facturas'
    raise_exception = True
    permission_required = 'compras.delete_facturadecompra'
    redirect_field_name = '/login/'
