from django import forms

from .models import Producto

class Add_form(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('codigo', 'nombre','descripcion','cantidad')