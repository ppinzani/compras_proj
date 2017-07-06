from django.views.generic import ListView
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Mercaderia, CategoriaMercaderia
from .forms import MercaderiaForm, CategoriaForm


# Create your views here.
class MercaderiasList(LoginRequiredMixin, ListView):
    model = Mercaderia
    template_name = 'mercaderias/mercaderias_lista.html'
    #This setting gives the queried data a helpful name.
    #This name can then be later used in templates.
    context_object_name = 'mercaderias'
    redirect_field_name = '/login/'


class ActualizarMercaderia(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = MercaderiaForm
    template_name = 'mercaderias/create_update_mercaderias.html'
    model = Mercaderia
    success_url = '/mercaderias/'
    permission_required = 'mercaderias.change_mercaderia'
    raise_exception = True


class EliminarMercaderia(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mercaderia
    success_url = '/mercaderias/'
    template_name = 'mercaderias/eliminar_mercaderia.html'
    permission_required = 'mercaderias.delete_mercaderia'
    raise_exception = True


class CrearMercaderia(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = MercaderiaForm
    template_name = 'mercaderias/create_update_mercaderias.html'
    model = Mercaderia
    success_url = '/mercaderias/'
    permission_required = 'mercaderias.add_mercaderia'
    raise_exception = True


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


class CrearCategoria(LoginRequiredMixin, CreateView):
    form_class = CategoriaForm
    template_name = 'mercaderias/create_update_categorias.html'
    model = CategoriaMercaderia
    success_url = '/mercaderias/categorias/'
    permission_required = 'mercaderias.add_categoriamercaderia'
    raise_exception = True
