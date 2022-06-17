from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from apps.principal.models import *

class ConductorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Conductor
        fields = ('id','nombre','apellido1','apellido2','email','telefono','uid_firebase')


class TransportistaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transportista
        fields = ('__all__')

class CamionSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Camion
        fields = ('id','marca','modelo','tara','mma','pesomercanciamax','alto','ancho','largo','volumenmercanciamax','litrosdeposito','matricula','kilometros','transportista')

class ClienteSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Cliente
        fields = ('dni','nombre','apellido1','apellido2','direccion','provincia','poblacion','cp','email','movil','lat','lon')

class AlbaranSerializer(serializers.ModelSerializer):

    cliente_dni = ClienteSerializer()
    class Meta:
        model = Albaran
        fields = ('id','fechaentrega','horamin','horamax','cliente_dni','estado')

class RutaSerializer(serializers.ModelSerializer): 

    transportista = TransportistaSerializer()
    camion = CamionSerializer()
    albaran = AlbaranSerializer()
    conductor = ConductorSerializer()
    fecharuta = serializers.DateField()

    class Meta:
        model = Ruta
        fields = '__all__'

class RutaAgrupadasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ruta

        fields = ('id','transportista_id','camion_id','conductor_id','fecharuta')


    

