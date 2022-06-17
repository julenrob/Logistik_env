from django.urls import path
# from .views import ConductorListView, ConductorCreateView, ConductorRetrieveView, ConductorUpdateView, ConductorDestroyView
from .views import *

urlpatterns = [
    path('conductores/', ConductorListView.as_view(), name='conductores'),
    path('conductores/create', ConductorCreateView.as_view(), name='conductores_create'),
    
    path('camiones/', CamionListView.as_view(), name='camiones'),
    path('conductor/<str:uid_firebase>/', ConductorRetrieveView.as_view(), name='conductor'),
    path('rutas_agrupadas/', RutasAgrupadasByConductorListAPIView.as_view(), name='rutas_agrupadas'),
    path('rutas/', RutasByConductorFechaListAPIView.as_view(), name='rutas'),

    path('conductor/<str:uid_firebase>/update', ConductorUpdateView.as_view(), name='conductor_update'),
    path('conductor/<str:uid_firebase>/delete', ConductorDestroyView.as_view(), name='conductor_delete'),
]