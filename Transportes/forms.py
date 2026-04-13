from Administracion.models import *
from django import forms

class AutobusForm(forms.ModelForm):
    class Meta:
        model = Autobus
        fields = '__all__'

class PasajeroForm(forms.ModelForm):
    
    class Meta:
        model = Pasajero
        fields = '__all__'

class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = '__all__'

class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = '__all__'
        
        widgets = {
            'fecha_y_hora': forms.DateTimeInput(attrs={
                'type': 'datetime-local'
            })
        }

class BoletoForm(forms.ModelForm):
    class Meta:
        model = Boleto
        fields = ['numero_asiento', 'pasajero']
