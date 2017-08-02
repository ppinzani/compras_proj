from django import forms

from .models import Proveedor
from proj_compras.constants import CONDICION_IVA_CHOICES
#from proj_compras.constants import RESPONSABLE_INSCRIPTO


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor

        fields = ('nombre_fiscal', 'nombre_fantasia', 'fecha_alta',
                  'cuit', 'condicion_iva', )

        widgets = {
            'condicion_iva': forms.Select(attrs={
                            'placeholder': 'Condición IVA',
                            'class': 'form-control'})
        }

    nombre_fantasia = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de Fantasía'})
    )
    nombre_fiscal = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre Fiscal'})
    )
    fecha_alta = forms.DateField(
        required=False,
        label='Fecha De Alta',
        widget=forms.DateInput(attrs={
                               'placeholder': 'Fecha de Alta',
                               'class': 'form-control',
                               'id': 'FechaAlta'})
    )
    cuit = forms.CharField(
        required=False,
        label='CUIT',
        widget=forms.TextInput(attrs={'placeholder': 'CUIT'})
    )
    #margen_ganancia = forms.IntegerField(
    #    widget=forms.NumberInput(attrs={'placeholder': 'form-control'})
    #)
