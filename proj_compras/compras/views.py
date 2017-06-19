from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.db import IntegrityError, transaction
from django.contrib import messages
from django.views.generic import ListView, DeleteView, RedirectView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse

from proj_compras.constants import APROBADO, RECHAZADO
from .models import SolicitudDeCompra, DetalleSolicitud
from .models import Cotizacion, DetalleCotizacion
from .forms import DetalleSolicitudForm, SolicitudDeCompraForm
from .forms import BaseSolicitudFormSet, BaseCotizacionFormSet
from .forms import CotizacionForm, DetalleCotizacionForm


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
        solicitud.estado = APROBADO
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
            if solicitud_form.cleaned_data['estado'] == APROBADO:
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
            solicitud_form = SolicitudDeCompraForm(initial={'generada_por': request.user.pk},
                                                   instance=solicitud)

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

    total = 0
    for d in detalles:
        total = total + d.get_subtotal()

    variables = {
        'cotizacion': cotizacion,
        'detalles': detalles,
        'total': total
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
        cotizacion.estado = APROBADO
        cotizacion.modificado_por = self.request.user
        cotizacion.save()
        return super(AprobarCotizacion, self).get_redirect_url(*args,**kwargs)


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
        cotizacion.estado = RECHAZADO
        cotizacion.modificado_por = self.request.user
        cotizacion.save()
        return super(RechazarCotizacion, self).get_redirect_url(*args,**kwargs)


@login_required()
def cotizacion_cru(request, pk=None):

    DetalleFormSet = formset_factory(DetalleCotizacionForm,
                                     formset=BaseCotizacionFormSet)

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
            cotizacion.estado = cotizacion_form.cleaned_data['estado']
            cotizacion.proveedor = cotizacion_form.cleaned_data['proveedor']
            if cotizacion_form.cleaned_data['estado'] == APROBADO:
                if not request.user.has_perm('compras.puede_aprobar_cotizacion'):
                    return HttpResponseForbidden()
            #    solicitud.aprobada_por = request.user
            #else:
            #    solicitud.aprobada_por = None
            cotizacion.save()

            nuevos_detalles = []

            for detalle_form in detalle_formset:
                cantidad = detalle_form.cleaned_data.get('cantidad')
                mercaderia = detalle_form.cleaned_data.get('mercaderia')
                precio = detalle_form.cleaned_data.get('precio')

                if cantidad and mercaderia and precio:
                    nuevos_detalles.append(DetalleCotizacion(cantidad=cantidad,
                                                             mercaderia=mercaderia,
                                                             precio=precio,
                                                             cotizacion=cotizacion))

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
