from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *

class ExtendedUserInline(admin.StackedInline):
    model = ExtendedUser
    can_delete = False
    verbose_name_plural = 'Extended Users'

class CustomizedUserAdmin(UserAdmin):
    inlines = (ExtendedUserInline, )

class TransportistaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','direccion','provincia','poblacion','cp')

class CamionAdmin(admin.ModelAdmin):
    list_display = ('id','marca','modelo','tara','mma', 'pesomercanciamax','alto','ancho','largo','volumenmercanciamax','litrosdeposito','matricula','kilometros','transportista_id')

class ConductorAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'apellido1','apellido2')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre', 'apellido1','apellido2','direccion', 'provincia', 'poblacion', 'cp', 'movil')

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'descripcion')

class AlbaranAdmin(admin.ModelAdmin):
    list_display = ('id','fechaentrega', 'horamin','horamax','cliente_dni', 'estado_id')

class MercanciaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion', 'peso','cantidad','volumen', 'fechaentregaaprox', 'cliente_dni', 'albaran_id')

class ConductoresConducenCamionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'camion_id', 'conductor_id')

class RutaAdmin(admin.ModelAdmin):
    list_display = ('id','transportista_id', 'camion_id', 'albaran_id', 'fecharuta')

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(ExtendedUser)

admin.site.register(Transportista, TransportistaAdmin)
admin.site.register(Camion, CamionAdmin)
admin.site.register(Conductor, ConductorAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Albaran, AlbaranAdmin)
admin.site.register(Mercancia, MercanciaAdmin)
admin.site.register(ConductoresConducenCamiones, ConductoresConducenCamionesAdmin)
admin.site.register(Ruta, RutaAdmin)
