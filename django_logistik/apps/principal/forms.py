from django import forms
from .models import *
# from .models import Transportista
# from .models import Camion
# from .models import Conductor
# from .models import Cliente
# from .models import Estado
# from .models import Albaran
# from .models import Mercancia

class TransportistaForm(forms.ModelForm):
    class Meta:
        model = Transportista
        # fields = '__all__'
        fields = ('nombre','direccion','provincia','poblacion','cp')

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        # fields = '__all__'
        fields = ('marca','modelo','tara','mma','alto','ancho','largo','litrosdeposito','matricula','kilometros','transportista')

class ConductorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Conductor
        # fields = '__all__'
        fields = ('nombre','apellido1','apellido2','email','password','telefono')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        # fields = '__all__'
        fields = ('dni','nombre','apellido1','apellido2','direccion','provincia','poblacion','cp','email','movil')

# class EstadoForm(forms.ModelForm):
#     class Meta:
#         model = Estado
#         fields = '__all__'

class AlbaranForm(forms.ModelForm):
    class Meta:
        model = Albaran
        fields = ('fechaentrega','horamin','horamax','cliente_dni')

class MercanciaForm(forms.ModelForm):
    class Meta:
        model = Mercancia
        fields = '__all__'

# class SelectAlbaranForm(forms.ModelForm):
#     class Meta:
#         model = Albaran
#         fields = 

class ConductoresConducenCamionesForm(forms.ModelForm):
    class Meta:
        model = ConductoresConducenCamiones
        fields = '__all__'

class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = '__all__'