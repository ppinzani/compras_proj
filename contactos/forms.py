from django import forms

from .models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'telefono', 'direccion',
                  'pagina_web', 'detalles', 'proveedor')
        widgets = {
            'nombre': forms.TextInput(
                attrs={'placeholder': 'Nombre', 'class': 'form-control'}
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email', 'class': 'form-control'}
            ),
            'telefono': forms.TextInput(
                attrs={'placeholder': 'Telefono', 'class': 'form-control'}
            ),
            'direccion': forms.TextInput(
                attrs={'placeholder': 'Direccion', 'class': 'form-control'}
            ),
            'pagina_web': forms.TextInput(
                attrs={'placeholder': 'Direccion Web', 'class': 'form-control'}
            ),
            'detalles': forms.Textarea(
                attrs={'placeholder': 'Detalles', 'class': 'form-control'}
            ),
        }
