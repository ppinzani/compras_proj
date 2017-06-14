from django import forms
from django.forms.formsets import BaseFormSet
from django.contrib.auth import get_user_model

from .models import SolicitudDeCompra, DetalleSolicitud

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
        fields = ('generada_por', 'observaciones',)
        widgets = {
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
