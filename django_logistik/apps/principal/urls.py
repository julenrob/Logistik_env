from django.urls import path, include
from .views import *
from apps.principal.mercancia_view import MercanciaUpdate
from django.contrib import admin

urlpatterns = [
    path('', home, name="home"),
    # path('admin/', admin.site.urls),

    path('crear_transportista/', crear_transportista, name="crear_transportista"),
    path('crear_camion/', crear_camion, name="crear_camion"),
    path('crear_conductor/', crear_conductor, name="crear_conductor"),
    path('crear_cliente/', crear_cliente, name="crear_cliente"),
    path('crear_albaran/', crear_albaran, name="crear_albaran"),
    path('crear_mercancia/', crear_mercancia, name="crear_mercancia"),
    path('crear_ruta/', crear_ruta, name="crear_ruta"),

    # path('modificar_mercancia/<int:pk>/', MercanciaUpdate.as_view(), name="modificar_mercancia"),
    path('modal_modificar_mercancia/', modal_modificar_mercancia, name="modal_modificar_mercancia"),
    path('modal_modificar_mercancia/<int:pk>/', MercanciaUpdate.as_view(), name="modificar_mercancia"),
     
    path('listar_transportistas/', listar_transportistas, name="listar_transportistas"),
    path('listar_conductores/', listar_conductores, name="listar_conductores"),
    path('listar_camiones/', listar_camiones, name="listar_camiones"),
    path('listar_clientes/', listar_clientes, name="listar_clientes"),
    path('listar_albaranes/', listar_albaranes, name="listar_albaranes"),
    path('listar_mercancias/', listar_mercancias, name="listar_mercancias"),
    path('listar_rutas/', listar_rutas, name="listar_rutas"),
    
    path('accounts/', include('django.contrib.auth.urls')),

    
]
