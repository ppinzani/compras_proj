from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,  HttpResponseForbidden, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import DeleteView

from .models import Contacto
from .forms import ContactoForm
from proj_compras.proveedores.models import Proveedor


#@login_required()
def detalle_contacto(request, uuid):

    contacto = Contacto.objects.get(uuid=uuid)

    template = 'contactos/detalle_contacto.html'

    variables = {
        'contacto': contacto,
    }

    return render(request, template, variables)


#@login_required()
def contacto_cru(request, uuid=None, proveedor=None):

    if uuid:  # Si hay uuid estoy editando
        contacto = get_object_or_404(Contacto, uuid=uuid)
        #if contacto.owner != request.user:
        #    return HttpResponseForbidden()
    else:
        contacto = Contacto()

    if request.POST:
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            proveedor = form.cleaned_data['proveedor']
            #if account.owner != request.user:
            #    return HttpResponseForbidden()
            # save the data
            contacto = form.save()

            if request.is_ajax():
                return render(request,
                              'contactos/item_contacto.html',
                              {'proveedor': proveedor, 'contacto': contacto})
            else:
                reverse_url = reverse(
                    'proveedores:detalle',
                    args=(proveedor.uuid,)
                )
                return HttpResponseRedirect(reverse_url)
        else:
            # if the form isn't valid, still fetch the
            # account so it can be passed to the template
            proveedor = form.cleaned_data['proveedor']
    else:
        form = ContactoForm(instance=contacto)

    # this is used to fetch the account if it exists as a URL parameter
    if request.GET.get('proveedor', ''):
        proveedor = Proveedor.objects.get(id=request.GET.get('proveedor', ''))

    variables = {
        'form': form,
        'contacto': contacto,
        'proveedor': proveedor,
    }

    if request.is_ajax():
        template = 'contactos/item_contacto_form.html'
    else:
        template = 'contactos/contacto_cru.html'

    return render(request, template, variables)


#Create Mixin to subclass with Deleteview
class ContactoMixin(object):
    model = Contacto

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Contacto'})
        return kwargs

    # @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactoMixin, self).dispatch(*args, **kwargs)


class BorrarContacto(ContactoMixin, DeleteView):
    template_name = 'confirmar_objeto_eliminado.html'

    def get_object(self, queryset=None):
        obj = super(BorrarContacto, self).get_object()
        #if not obj.owner == self.request.user:
        #    raise Http404
        proveedor = Proveedor.objects.get(id=obj.proveedor.id)
        self.proveedor = proveedor
        return obj

    def get_success_url(self):
        return reverse(
            'proveedores:detalle',
            args=(self.proveedor.uuid,)
        )
