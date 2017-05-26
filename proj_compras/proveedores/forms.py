from django import forms

from .models import Proveedor
from proj_compras.constants import CONDICION_IVA_CHOICES
from proj_compras.constants import RESPONSABLE_INSCRIPTO


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor

        fields = ('nombre_fiscal', 'nombre_fantasia', 'fecha_alta',
                  'cuit', 'condicion_iva', )

        nombre_fantasia = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        nombre_fiscal = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        fecha_alta = forms.DateField(
            widget=forms.DateInput(attrs={'class': 'form-control'})
        )
        cuit = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        #margen_ganancia = forms.IntegerField(
        #    widget=forms.NumberInput(attrs={'class': 'form-control'})
        #)
        condicion_iva = forms.MultipleChoiceField(
            choices=CONDICION_IVA_CHOICES,
            widget=forms.SelectMultiple(attrs={'class': 'form-control'})
        )
