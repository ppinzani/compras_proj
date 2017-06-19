from django import forms
from django.forms.formsets import BaseFormSet
from django.contrib.auth import get_user_model

from .models import SolicitudDeCompra, DetalleSolicitud
from .models import Cotizacion, DetalleCotizacion
from proveedores.models import Proveedor

User = get_user_model()


class DetalleSolicitudForm(forms.ModelForm):
    class Meta:
        model = DetalleSolicitud
        fields = ('cantidad', 'mercaderia',)
        widgets = {
            'cantidad': forms.TextInput(
                attrs={'placeholder': 'Cantidad', 'class': 'form-control'}
            ),
            'mercaderia': forms.Select(
                attrs={'placeholder': 'Detalle', 'class': 'form-control'}
            ),
        }


class SolicitudDeCompraForm(forms.ModelForm):
    class Meta:
        model = SolicitudDeCompra
        fields = ('estado', 'generada_por', 'observaciones',)
        widgets = {
            'estado': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'observaciones': forms.Textarea(
                attrs={'class': 'form-control'}
            ),
        }

    generada_por = forms.ModelChoiceField(queryset=User.objects.all(),
                                          widget=forms.Select(attrs={
                                              'class': 'form-control'}))


class BaseSolicitudFormSet(BaseFormSet):
    def clean(self):
        '''
        Agrego validacion para que no se repita mercaderia en 2 items
        distintos y que no haya items vacios.
        '''
        if any(self.errors):
            return

        mercaderias = []
        duplicados = False

        for form in self.forms:
            cantidad = form.cleaned_data.get('cantidad')
            mercaderia = form.cleaned_data.get('mercaderia')

            #Chequeo que no haya mercaderias repetidas
            if cantidad and mercaderia:
                if mercaderia in mercaderias:
                    duplicados = True
                mercaderias.append(mercaderia)

            if duplicados:
                raise forms.ValidationError(
                    'No se debe repetir la mercaderia en 2 items distintos.',
                    code='mercaderia_duplicada'
                )
            #Chequeo que esten completas la cantidad y detalle
            if cantidad and not mercaderia:
                raise forms.ValidationError(
                    'El campo de detalle esta vacio.',
                    code='mercaderia_vacio'
                )

            if not cantidad and mercaderia:
                raise forms.ValidationError(
                    'El campo de cantidad esta vacio.',
                    code='cantidad_vacio'
                )


#Cotizaciones
class DetalleCotizacionForm(forms.ModelForm):
    class Meta:
        model = DetalleCotizacion
        fields = ('cantidad', 'mercaderia', 'precio',)
        widgets = {
            'cantidad': forms.TextInput(
                attrs={'placeholder': 'Cantidad', 'class': 'form-control'}
            ),
            'mercaderia': forms.Select(
                attrs={'placeholder': 'Detalle', 'class': 'form-control'}
            ),
            'precio': forms.NumberInput(
                attrs={'placeholder': 'Precio Unitario',
                       'class': 'form-control'}
            ),
        }


class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ('estado', 'proveedor')
        widgets = {
            'estado': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }

    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(),
                                       widget=forms.Select(attrs={
                                       'class': 'form-control'}))


class BaseCotizacionFormSet(BaseFormSet):
    def clean(self):
        '''
        Agrego validacion para que no se repita mercaderia en 2 items
        distintos y que no haya items vacios.
        '''
        if any(self.errors):
            return

        mercaderias = []
        duplicados = False

        for form in self.forms:
            cantidad = form.cleaned_data.get('cantidad')
            mercaderia = form.cleaned_data.get('mercaderia')
            precio = form.cleaned_data.get('precio')

            #Chequeo que no haya mercaderias repetidas
            if cantidad and mercaderia and precio:
                if mercaderia in mercaderias:
                    duplicados = True
                mercaderias.append(mercaderia)

            if duplicados:
                raise forms.ValidationError(
                    'No se debe repetir la mercaderia en 2 items distintos.',
                    code='cotizacion_mercaderia_duplicada'
                )

            #Si nunguno de los campos esta completo no hay problema
            # Ignoro la entrada
            if not mercaderia and not cantidad and not precio:
                continue

            #Chequeo que esten completas la cantidad y detalle y precio
            if not mercaderia:
                raise forms.ValidationError(
                    'El campo de detalle esta vacio.',
                    code='cotizacion_mercaderia_vacio'
                )

            if not cantidad:
                raise forms.ValidationError(
                    'El campo de cantidad esta vacio.',
                    code='cotizacion_cantidad_vacio'
                )

            if not precio:
                raise forms.ValidationError(
                    'El campo de precio unitario esta vacio.',
                    code='cotizacion_precio_vacio'
                )
