from django import forms
from .models import Cartera, Billetera, Cinto

class CarteraForm(forms.ModelForm):
    class Meta:
        model = Cartera
        fields = '__all__'

class BilleteraForm(forms.ModelForm):
    class Meta:
        model = Billetera
        fields = '__all__'

class CintoForm(forms.ModelForm):
    class Meta:
        model = Cinto
        fields = '__all__'

class BuscarForm(forms.Form):
    nombre = forms.CharField(label="Buscar Cartera", max_length=100)
