from django import forms

from .models import Mercaderia, CategoriaMercaderia


class MercaderiaForm(forms.ModelForm):
    class Meta:
        model = Mercaderia
        fields = ('descripcion', 'categoria')
        widgets = {
            'descripcion': forms.TextInput(
                attrs={'placeholder': 'Descripción', 'class': 'form-control'}
            ),
            'categoria': forms.Select(
                attrs={'placeholder': 'Categoria', 'class': 'form-control'}
            ),
        }


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
