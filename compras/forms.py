from django import forms
from django.forms.formsets import BaseFormSet
from django.contrib.auth import get_user_model

from .models import SolicitudDeCompra, DetalleSolicitud
from .models import Cotizacion, DetalleCotizacion
from .models import OrdenDeCompra, PagoDeCompra
from .models import FacturaDeCompra
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
        fields = ('estado', 'proveedor', 'descuento')
        widgets = {
            'estado': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'descuento': forms.NumberInput(
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


class OrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = OrdenDeCompra
        fields = ('numero', 'forma_de_pago', 'cuotas')
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'forma_de_pago': forms.Select(
                attrs={'class': 'form-control',
                       'id': 'id_forma_de_pago_form'}
            ),
            'cuotas': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id_pago_cuotas',
                }
            ),
        }


class PagoDeCompraForm(forms.ModelForm):
    class Meta:
        model = PagoDeCompra
        fields = ('fecha_de_pago', 'importe', 'estado')
        widgets = {
            'fecha_de_pago': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Vencimiento'
                }
            ),
            'importe': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Importe'
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Estado'
                }
            ),
        }


class BasePagoFormSet(BaseFormSet):
    def clean(self):
        '''
        Agrego validacion para que no haya precio o fecha vacio
        '''
        if any(self.errors):
            return

        for form in self.forms:
            importe = form.cleaned_data.get('importe')
            fecha = form.cleaned_data.get('fecha_de_pago')

            #Chequeo que esten completas la cantidad y detalle
            if importe and not fecha:
                raise forms.ValidationError(
                    'El campo de vencimiento esta vacio.',
                    code='fecha_vencimiento_vacio'
                )

            if not importe and fecha:
                raise forms.ValidationError(
                    'El campo de impoprte esta vacio.',
                    code='importe_vacio'
                )


class FacturaDeCompraForm(forms.ModelForm):
    class Meta:
        model = FacturaDeCompra
        fields = ('numero', 'fecha', 'importe', 'foto', 'tipo')
        widgets = {
            'numero': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fecha': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'importe': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
