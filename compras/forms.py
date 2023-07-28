from django import forms
from .models import Auto, Cliente, Compra


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = "__all__"


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = "__all__"


class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100, required=False)
