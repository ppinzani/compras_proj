from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from .models import Proveedor
from .models import ContactoProveedor
from .forms import ProveedorForm


# Create your views here.
class ProveedoresList(ListView):
    model = Proveedor
    paginate_by = 12  # Para agregar paginacion
    template_name = 'proveedores/proveedores_list.html'
    #This setting gives the queried data a helpful name.
    #This name can then be later used in templates.
    context_object_name = 'proveedores'

    def get_queryset(self):
        try:
            a = self.request.GET.get('proveedor',)
        except KeyError:
            a = None
        if a:
            proveedores_list = Proveedor.objects.filter(
                nombre_fiscal__icontains=a,
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

#    @method_decorator(login_required) No lo uso por ahora
#       def dispatch(self, *args, **kwargs):
#       return super(ProveedoresList, self).dispatch(*args, **kwargs)


#@login_required()
def detalle_proveedor(request, uuid):
    #The uuid object is passed to the view via the URL configuration
    proveedor = Proveedor.objects.get(uuid=uuid)

    #contactos = ContactoProveedor.objects.filter(proveedor=proveedor)

    variables = {
        'proveedor': proveedor,
        #'contactos': contactos
    }

    return render(request, 'proveedores/detalle_proveedor.html', variables)


#@login_required()
def proveedor_cru(request, uuid=None):

    if uuid:
        proveedor = get_object_or_404(Proveedor, uuid=uuid)
        #if account.owner != request.user:
        #    return HttpResponseForbidden()
    else:
        proveedor = Proveedor()

    if request.POST:
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save(commit=False)
            if not form['nombre_fantasia']:
                form['nombre_fantasia'] = form['nombre_fiscal']
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
