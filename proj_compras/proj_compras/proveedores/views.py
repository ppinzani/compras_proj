from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Proveedor


# Create your views here.
class ProveedoresList(ListView):
    model = Proveedor
    paginate_by = 12  # Para agregar paginacion
    template_name = 'proveedores/proveedores_list.html'
    #This setting gives the queried data a helpful name.
    #This name can then be later used in templates.
    context_object_name = 'proveedores'

'''
El comportamiento por default es este
    def get_queryset(self):
        proveedores_list = Proveedor.objects.all()
        return proveedores_list
'''

#    @method_decorator(login_required) No lo uso por ahora
#       def dispatch(self, *args, **kwargs):
#       return super(ProveedoresList, self).dispatch(*args, **kwargs)
