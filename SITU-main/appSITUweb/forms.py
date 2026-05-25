from django import forms
from .models import Pasajero, Bus, Viaje

class PasajeroFormulario(forms.ModelForm):
	class Meta:
		model = Pasajero
		fields=["cedula","nombre","apellido", "email","imagen"]

class BusFormulario(forms.ModelForm):
	class Meta:
		model = Bus
		fields=["placa","cooperativa","numero"]

class ViajeFormulario(forms.ModelForm):
	class Meta:
		model = Viaje
		fields=["pasajero","bus","costo","cantidad","efectivo","tipo"]