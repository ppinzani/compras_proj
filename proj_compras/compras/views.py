from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.db import IntegrityError, transaction
from django.contrib import messages
from django.views.generic import ListView, DeleteView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden


from .models import SolicitudDeCompra, DetalleSolicitud
from .forms import DetalleSolicitudForm, SolicitudDeCompraForm, BaseSolicitudFormSet


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


class BorrarSolicitudDeCompra(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = SolicitudDeCompra
    template_name = 'compras/eliminar_solicitud.html'
    permission_required = 'compras.delete_solicituddecompras'
    raise_exception = True
    success_url = '/compras/solicitudes/'

# Create your views here.
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
        solicitud_form = SolicitudDeCompraForm(request.POST, instance=solicitud)
        detalle_formset = DetalleFormSet(request.POST)

        if solicitud_form.is_valid() and detalle_formset.is_valid():
            #Guardo los detalles de la solicitud
            solicitud.generada_por = solicitud_form.cleaned_data['generada_por']
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
                            #Fixme no puedo agregar los nuevos??
                            DetalleSolicitud.objects.filter(solicitud=solicitud).delete()
                            DetalleSolicitud.objects.bulk_create(nuevos_detalles)

                            # And notify our users that it worked
                            messages.success(request, 'Solicitud Grabada!')
                    except IntegrityError:
                        messages.error(request, 'Error grabando la solicitud!')
                        return redirect(reverse('compras:lista_solicitudes'))

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
        'detalles': detalles,
    }

    template = 'compras/create_update_solicitud.html'

    return render(request, template, variables)
