from django.views.generic import ListView
from braces.views import LoginRequiredMixin


# Create your views here.
class ProveedoresList(LoginRequiredMixin, ListView):
    model = Proveedor
    paginate_by = 12  # Para agregar paginacion
    template_name = 'mercaderias/mercaderias_list.html'
    #This setting gives the queried data a helpful name.
    #This name can then be later used in templates.
    context_object_name = 'mercaderias'
    redirect_field_name = '/login/'

    '''
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
