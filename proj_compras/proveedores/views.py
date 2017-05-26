from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.db.models import Q
from braces.views import LoginRequiredMixin


from .models import Proveedor
from proj_compras.contactos.models import Contacto
from .forms import ProveedorForm


# Create your views here.
class ProveedoresList(LoginRequiredMixin, ListView):
    model = Proveedor
    paginate_by = 12  # Para agregar paginacion
    template_name = 'proveedores/proveedores_list.html'
    #This setting gives the queried data a helpful name.
    #This name can then be later used in templates.
    context_object_name = 'proveedores'
    redirect_field_name = '/login/'

    def get_queryset(self):
        try:
            a = self.request.GET.get('proveedor',)
        except KeyError:
            a = None
        if a:
            proveedores_list = Proveedor.objects.filter(
                Q(nombre_fiscal__icontains=a) |
                Q(nombre_fantasia__icontains=a)
            )
        else:
            proveedores_list = Proveedor.objects.all()
        return proveedores_list

'''
El comportamiento por default es este
    def get_queryset(self):
        proveedores_list = Proveedor.objects.all()
        return proveedores_list
'''


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
        if not request.user.has_perm('proveedores.can_edit'):
            return HttpResponseForbidden()
        proveedor = get_object_or_404(Proveedor, uuid=uuid)
    else:
        if not request.user.has_perm('proveedores.can_add'):
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

    if request.is_ajax():
        template = 'proveedores/item_proveedor_form.html'
    else:
        template = 'proveedores/proveedor_cru.html'

    return render(request, template, variables)
