from django import forms

from .models import Mercaderia, CategoriaMercaderia
from proveedores.models import Proveedor


class MercaderiaForm(forms.ModelForm):
    class Meta:
        model = Mercaderia
        fields = ('descripcion', 'iva')
        widgets = {
            'descripcion': forms.TextInput(
                attrs={'placeholder': 'Descripción', 'class': 'form-control'}
            ),
            'iva': forms.NumberInput(
                attrs={'placeholder': 'Iva', 'class': 'form-control'}
            ),
        }

    proveedores = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'id_form_add_proveedor',
            }
        ),
        required=False
    )

    categorias = forms.ModelChoiceField(
        queryset=CategoriaMercaderia.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'id_form_add_categoria',
            }
        ),
        required=False
    )


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaMercaderia
        fields = ('nombre', 'padre')
        widgets = {
            'nombre': forms.TextInput(
                attrs={'placeholder': 'Nombre de la Categoria',
                       'class': 'form-control'}
            ),
            'padre': forms.Select(
                choices=CategoriaMercaderia.objects.all().values_list('id', 'nombre'),
                attrs={'placeholder': 'Padre', 'class': 'form-control'}
            ),
        }
