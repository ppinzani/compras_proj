from django.views.generic import ListView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.db.models import Q
from braces.views import LoginRequiredMixin, PermissionRequiredMixin


from .models import Proveedor
from contactos.models import Contacto
from .forms import ProveedorForm


# Create your views here.
class ProveedoresList(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'proveedores/proveedores_lista.html'
    #This name can then be later used in templates.
    context_object_name = 'proveedores'
    redirect_field_name = '/login/'


@login_required()
def detalle_proveedor(request, uuid):
    #The uuid object is passed to the view via the URL configuration
    proveedor = Proveedor.objects.get(uuid=uuid)

    contactos = Contacto.objects.filter(proveedor=proveedor)

    variables = {
        'proveedor': proveedor,
        'contactos': contactos
    }

    return render(request, 'proveedores/detalle_proveedor.html', variables)


@login_required()
def proveedor_cru(request, uuid=None):

    if uuid:
        if not request.user.has_perm('proveedores.change_proveedor'):
            return HttpResponseForbidden()
        proveedor = get_object_or_404(Proveedor, uuid=uuid)
    else:
        if not request.user.has_perm('proveedores.add_proveedor'):
            return HttpResponseForbidden()
        proveedor = Proveedor()

    if request.POST:
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            redirect_url = reverse(
                'proveedores:detalle',
                args=(proveedor.uuid,)
            )
            return HttpResponseRedirect(redirect_url)
    else:
        form = ProveedorForm(instance=proveedor)

    variables = {
        'form': form,
        'proveedor': proveedor,
    }

    template = 'proveedores/proveedores_create_update.html'

    return render(request, template, variables)


class BorrarProveedor(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Proveedor
    template_name = 'proveedores/eliminar_proveedor.html'
    permission_required = 'proveedores.delete_proveedor'
    raise_exception = True
    success_url = '/proveedores/'
