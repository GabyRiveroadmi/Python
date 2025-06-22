from django import forms
from .models import Cartera, Billetera, Cinto

class CarteraForm(forms.ModelForm):
    class Meta:
        model = Cartera
        fields = ['nombre', 'color', 'precio']

class BilleteraForm(forms.ModelForm):
    class Meta:
        model = Billetera
        fields = ['nombre', 'cuero', 'precio']

class CintoForm(forms.ModelForm):
    class Meta:
        model = Cinto
        fields = ['nombre', 'talle', 'precio']
