# from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from apps.principal.models import *
from datetime import datetime
from django.db.models import Count
from django.db.models import Q
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .serializers import *

# Listar todos los elementos.
class CamionListView(ListAPIView):
    serializer_class = CamionSerializer
    permission_classes = ()
    queryset = Camion.objects.all()

# Listar todos los elementos.
class ConductorListView(ListAPIView):
    serializer_class = ConductorSerializer
    permission_classes = ()
    queryset = Conductor.objects.all()

# Crear un elemento.
class ConductorCreateView(CreateAPIView):
    serializer_class = ConductorSerializer
    permission_classes = ()

# Obtener un elemento concreto mediante una query.
class ConductorRetrieveView(RetrieveAPIView):
    serializer_class = ConductorSerializer
    permission_classes = ()
    queryset = Conductor.objects.all()
    lookup_field = 'uid_firebase'

class RutasAgrupadasByConductorListAPIView(ListAPIView):
    serializer_class = RutaAgrupadasSerializer
    
    def get_queryset(self):
        queryset = (Ruta.objects
                .filter(albaran__estado_id=2)
                .filter(albaran__fechaentrega__gte=datetime.now().date())
                .values('fecharuta', 'transportista_id','camion_id','conductor_id')
                .annotate(Count('fecharuta')) 
                .order_by()
                # .prefetch_related('transportista')
            )

        return queryset

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['conductor']

# Obtener las Rutas by conductor_id donde los albaranes estén en estado Asignado y la fecha sea igual o posterior a hoy
class RutasByConductorFechaListAPIView(ListAPIView):
    serializer_class = RutaSerializer

    def get_queryset(self):
        queryset = (Ruta.objects
            .filter(albaran__estado_id=2)
            .annotate(Count('fecharuta')) 
            .order_by('fecharuta')
        )

        return queryset

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['conductor','fecharuta']

# Obtener los albaranes by id con un poco de suerte al ir incluida la FK de cliente_id esto es ya todo el objeto y podemos acceder a las
# coordenadas.
class AlbaranesByIdListAPIView(ListAPIView):
    serializer_class = AlbaranSerializer
    queryset = Albaran.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

# Actualizar un elemento existente.
class ConductorUpdateView(UpdateAPIView):
    serializer_class = ConductorSerializer
    permission_classes = ()
    queryset = Conductor.objects.all()
    lookup_field = 'uid_firebase'

# Eliminar un elemento.
class ConductorDestroyView(DestroyAPIView):
    permission_classes = ()
    queryset = Conductor.objects.all()
    lookup_field = 'uid_firebase'
