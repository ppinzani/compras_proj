from django.views.generic import ListView
from django.views.generic import FormView, DeleteView, UpdateView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Mercaderia, CategoriaMercaderia, MercaderiaProveedor
from .forms import MercaderiaForm, CategoriaForm


# Create your views here.
class MercaderiasList(LoginRequiredMixin, ListView):
    model = Mercaderia
    template_name = 'mercaderias/mercaderias_lista.html'
    #This setting gives the queried data a helpful name.
    #This name can then be later used in templates.
    context_object_name = 'mercaderias'
    redirect_field_name = '/login/'


class ActualizarMercaderia(LoginRequiredMixin, PermissionRequiredMixin,
                           UpdateView):
    form_class = MercaderiaForm
    template_name = 'mercaderias/create_update_mercaderias.html'
    model = Mercaderia
    success_url = '/mercaderias/'
    permission_required = 'mercaderias.change_mercaderia'
    raise_exception = True


class EliminarMercaderia(LoginRequiredMixin, PermissionRequiredMixin,
                         DeleteView):
    model = Mercaderia
    success_url = '/mercaderias/'
    template_name = 'mercaderias/eliminar_mercaderia.html'
    permission_required = 'mercaderias.delete_mercaderia'
    raise_exception = True


@login_required
def mercaderias_create(request):

    if not request.user.has_perm('mercaderias.add_mercaderia'):
            return HttpResponseForbidden()
    mercaderia = Mercaderia()

    if request.POST:
        mercaderia_form = MercaderiaForm(request.POST, instance=mercaderia)
        if mercaderia_form.is_valid():
            mercaderia.descripcion = mercaderia_form.cleaned_data['descripcion']
            mercaderia.iva = mercaderia_form.cleaned_data['iva']
            mercaderia.save()
            if mercaderia_form.cleaned_data['categorias']:
                mercaderia.categorias.add(
                    mercaderia_form.cleaned_data['categorias']
                )
            if mercaderia_form.cleaned_data['proveedores']:
                mp = MercaderiaProveedor(
                    mercaderia=mercaderia,
                    proveedor=mercaderia_form.cleaned_data['proveedores'],
                    ultimo_precio=0
                )
                mp.save()
            mercaderia.save()
            return redirect('/mercaderias/')
    else:
        mercaderia_form = MercaderiaForm(instance=mercaderia)

    template = 'mercaderias/create_mercaderias.html'

    variables = {
        'mercaderia_form': mercaderia_form,
    }

    return render(request, template, variables)


@login_required
def mercaderias_edit(request, pk):
    if not request.user.has_perm('mercaderias.change_mercaderia'):
        return HttpResponseForbidden()
    mercaderia = get_object_or_404(Mercaderia, pk=pk)

    if request.POST:
        mercaderia_form = MercaderiaForm(request.POST, instance=mercaderia)
        if mercaderia_form.is_valid():
            mercaderia.descripcion = mercaderia_form.cleaned_data['descripcion']
            mercaderia.iva = mercaderia_form.cleaned_data['iva']
            if request.is_ajax():  # Si es ajax entonces estoy agregando cat o proveedor
                if request.POST['target'] == 'categoria':
                    mercaderia.categorias.add(
                        mercaderia_form.cleaned_data['categorias']
                    )
                    mercaderia.save()
                    template = 'mercaderias/mercaderia_categorias_items.html'
                    variables = {'categorias': mercaderia.categorias.all()}
                elif request.POST['target'] == 'proveedor':
                    mp = MercaderiaProveedor(
                        mercaderia=mercaderia,
                        proveedor=mercaderia_form.cleaned_data['proveedores'],
                        ultimo_precio=0
                    )
                    mp.save()
                    template = 'mercaderias/mercaderia_proveedor_items.html'
                    mps = MercaderiaProveedor.objects.filter(
                        mercaderia=mercaderia
                    )
                    variables = {'mps': mps}
                return render(request, template, variables)

            return redirect('/mercaderias/')
    else:
        mercaderia_form = MercaderiaForm(instance=mercaderia)

    template = 'mercaderias/update_mercaderias.html'
    categorias = mercaderia.categorias.all()
    mps = MercaderiaProveedor.objects.filter(mercaderia=mercaderia)

    variables = {
        'mercaderia_form': mercaderia_form,
        'categorias': categorias,
        'mps': mps,
    }

    return render(request, template, variables)


class CategoriasList(LoginRequiredMixin, ListView):
    model = CategoriaMercaderia
    template_name = 'mercaderias/categorias_lista.html'
    #This setting gives the queried data a helpful name.
    #This name can then be later used in templates.
    context_object_name = 'categorias'
    redirect_field_name = '/login/'


class ActualizarCategoria(LoginRequiredMixin, UpdateView):
    form_class = CategoriaForm
    template_name = 'mercaderias/create_update_categorias.html'
    model = CategoriaMercaderia
    success_url = '/mercaderias/categorias/'
    permission_required = 'mercaderias.change_categoriamercaderia'
    raise_exception = True


class EliminarCategoria(LoginRequiredMixin, DeleteView):
    model = CategoriaMercaderia
    success_url = '/mercaderias/categorias/'
    template_name = 'mercaderias/eliminar_categoria.html'
    permission_required = 'mercaderias.delete_categoriamercaderia'
    raise_exception = True


class CrearCategoria(LoginRequiredMixin, FormView):
    form_class = CategoriaForm
    template_name = 'mercaderias/create_update_categorias.html'
    model = CategoriaMercaderia
    success_url = '/mercaderias/categorias/'
    permission_required = 'mercaderias.add_categoriamercaderia'
    raise_exception = True
