from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,  HttpResponseForbidden, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import DeleteView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Contacto
from .forms import ContactoForm
from proveedores.models import Proveedor


@login_required()
def detalle_contacto(request, uuid):

    contacto = Contacto.objects.get(uuid=uuid)

    template = 'contactos/detalle_contacto.html'

    variables = {
        'contacto': contacto,
    }

    return render(request, template, variables)


@login_required()
def contacto_cru(request, uuid=None, proveedor=None):

    if uuid:  # Si hay uuid estoy editando
        if not request.user.has_perm('contactos.can_edit'):
                    return HttpResponseForbidden()
        contacto = get_object_or_404(Contacto, uuid=uuid)
    else:
        if not request.user.has_perm('contactos.can_edit'):
            return HttpResponseForbidden()
        contacto = Contacto()

    if request.POST:
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            proveedor = form.cleaned_data['proveedor']
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

    def dispatch(self, *args, **kwargs):
        return super(ContactoMixin, self).dispatch(*args, **kwargs)


class BorrarContacto(LoginRequiredMixin, PermissionRequiredMixin, ContactoMixin, DeleteView):
    template_name = 'confirmar_objeto_eliminado.html'
    permission_required = 'contactos.can_delete'
    raise_exception = True

    def get_object(self, queryset=None):
        obj = super(BorrarContacto, self).get_object()
        proveedor = Proveedor.objects.get(id=obj.proveedor.id)
        self.proveedor = proveedor
        return obj

    def get_success_url(self):
        return reverse(
            'proveedores:detalle',
            args=(self.proveedor.uuid,)
        )
