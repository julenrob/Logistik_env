from logging import disable
import requests
from django.contrib.auth.models import User
from django.db import models
import firebase_admin
from firebase_admin import credentials, auth

from django.dispatch import receiver
from django.db.models.signals import (
    post_save
)

class Transportista(models.Model):
    alava = 'Alava'
    albacete = 'Albacete'
    alicante = 'Alicante'
    almeria = 'Almeria'
    asturias = 'Asturias'
    avila = 'Avila'
    badajoz = 'Badajoz'
    barcelona = 'Barcelona'
    burgos = 'Burgos'
    caceres = 'Caceres'
    cadiz = 'Cadiz'
    cantabria = 'Cantabria'
    castellon = 'Castellon'
    ceuta = 'Ceuta'
    ciudad_real = 'Ciudad Real'
    cordoba = 'Cordoba'
    cuenca = 'Cuenca'
    girona = 'Girona'
    las_palmas = 'Las Palmas'
    granada = 'Granada'
    guadalajara = 'Guadalajara'
    guipuzcoa = 'Guipuzcoa'
    huelva = 'Huelva'
    huesca = 'Huesca'
    illes_balears = 'Illes Balears'
    jaen = 'Jaen'
    a_coruna = 'A Coruna'
    la_rioja = 'La Rioja'
    leon = 'Leon'
    lleida = 'Lleida'
    lugo = 'Lugo'
    madrid = 'Madrid'
    malaga = 'Malaga'
    melilla = 'Melilla'
    murcia = 'Murcia'
    navarra = 'Navarra'
    ourense = 'Ourense'
    palencia = 'Palencia'
    pontevedra = 'Pontevedra'
    salamanca = 'Salamanca'
    segovia = 'Segovia'
    sevilla = 'Sevilla'
    soria = 'Soria'
    tarragona = 'Tarragona'
    canarias = 'Santa Cruz de Tenerife'
    teruel = 'Teruel'
    toledo = 'Toledo'
    valencia = 'Valencia'
    valladolid = 'Valladolid'
    vizcaya = 'Vizcaya'
    zamora = 'Zamora'
    zaragoza = 'Zaragoza'

    PROVINCIAS = [
                (alava,'Álava'),
                (albacete,'Albacete'),
                (alicante,'Alicante'),
                (almeria,'Almería'),
                (asturias,'Asturias'),
                (avila,'Ávila'),
                (badajoz,'Badajoz'),
                (barcelona,'Barcelona'),
                (burgos,'Burgos'),
                (caceres,'Cáceres'),
                (cadiz,'Cádiz'),
                (cantabria,'Cantabria'),
                (castellon,'Castellón'),
                (ceuta,'Ceuta'),
                (ciudad_real,'Ciudad Real'),
                (cordoba,'Córdoba'),
                (cuenca,'Cuenca'),
                (girona,'Girona'),
                (las_palmas,'Las Palmas'),
                (granada,'Granada'),
                (guadalajara,'Guadalajara'),
                (guipuzcoa,'Guipúzcoa'),
                (huelva,'Huelva'),
                (huesca,'Huesca'),
                (illes_balears,'Illes Balears'),
                (jaen,'Jaén'),
                (a_coruna,'A Coruña'),
                (la_rioja,'La Rioja'),
                (leon,'León'),
                (lleida,'Lleida'),
                (lugo,'Lugo'),
                (madrid,'Madrid'),
                (malaga,'Málaga'),
                (melilla,'Melilla'),
                (murcia,'Murcia'),
                (navarra,'Navarra'),
                (ourense,'Ourense'),
                (palencia,'Palencia'),
                (pontevedra,'Pontevedra'),
                (salamanca,'Salamanca'),
                (segovia,'Segovia'),
                (sevilla,'Sevilla'),
                (soria,'Soria'),
                (tarragona,'Tarragona'),
                (canarias,'Santa Cruz de Tenerife'),
                (teruel,'Teruel'),
                (toledo,'Toledo'),
                (valencia,'Valencia'),
                (valladolid,'Valladolid'),
                (vizcaya,'Vizcaya'),
                (zamora,'Zamora'),
                (zaragoza,'Zaragoza')
    ]

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45)
    provincia = models.CharField(max_length=25, choices=PROVINCIAS)
    poblacion = models.CharField(max_length=45)
    cp = models.CharField(max_length=45)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'transportista'

class Camion(models.Model):
    id = models.BigAutoField(primary_key=True)
    marca = models.CharField(max_length=45, blank=True, null=True)
    modelo = models.CharField(max_length=45, blank=True, null=True)
    tara = models.FloatField(db_column='TARA', blank=True, null=True)  # Field name made lowercase.
    mma = models.FloatField(db_column='MMA', blank=True, null=True)  # Field name made lowercase.
    pesomercanciamax = models.FloatField(db_column='pesoMercanciaMax', blank=True, null=True)  # Field name made lowercase.
    alto = models.FloatField(blank=True, null=True)
    ancho = models.FloatField(blank=True, null=True)
    largo = models.FloatField(blank=True, null=True)
    volumenmercanciamax = models.FloatField(db_column='volumenMercanciaMax', blank=True, null=True)  # Field name made lowercase.
    litrosdeposito = models.FloatField(db_column='litrosDeposito', blank=True, null=True)  # Field name made lowercase.
    matricula = models.CharField(max_length=20, blank=True, null=True)
    kilometros = models.FloatField(blank=True, null=True)
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.matricula}'

    class Meta:
        managed = True
        db_table = 'camion'
        verbose_name_plural = 'Camiones'

class Conductor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido1 = models.CharField(max_length=45, blank=True, null=True)
    apellido2 = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField(max_length=40, null=False)
    password = models.CharField(max_length=40, null=False)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    uid_firebase = models.CharField(max_length=40, blank=True, null=True)

    conducido = models.ManyToManyField(
        Camion,
        through = 'ConductoresConducenCamiones',
        through_fields = ('conductor','camion'),
    )

    class Meta:
        managed = True
        db_table = 'conductor'
        verbose_name_plural = 'Conductores'
    
    def __str__(self):
        return f'{self.nombre} {self.apellido1}'

class ConductoresConducenCamiones(models.Model):
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f'{self.conductor} {self.camion} {self.fecha}'

    class Meta:
        managed = True
        db_table = 'conductores_conducen_camiones'
        unique_together = (('id', 'camion', 'conductor', 'fecha'))
        verbose_name_plural = 'Conductores conducen Camiones'


class Cliente(models.Model):
    dni = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=45)
    apellido1 = models.CharField(max_length=45)
    apellido2 = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45)
    provincia = models.CharField(max_length=45)
    poblacion = models.CharField(max_length=45)
    cp = models.CharField(max_length=45)
    email = models.EmailField(max_length=50, blank=False, null=False)
    movil = models.CharField(max_length=45, blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido1} {self.dni}'

    class Meta:
        managed = True
        db_table = 'cliente'

class Estado(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=90, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'estado'

class Albaran(models.Model):
    id = models.BigAutoField(primary_key=True)
    fechaentrega = models.DateField(db_column='fechaEntrega')
    horamin = models.TimeField(db_column='horaMin')
    horamax = models.TimeField(db_column='horaMax')
    cliente_dni = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cliente_dni')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.id} {self.fechaentrega} {self.estado} {self.cliente_dni}'

    class Meta:
        managed = True
        db_table = 'albaran'
        verbose_name_plural = 'Albaranes'

class Ruta(models.Model):
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    albaran = models.ForeignKey(Albaran, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    fecharuta = models.DateField(db_column='fechaRuta')

    class Meta:
        managed = True
        db_table = 'ruta'
        unique_together = (('transportista', 'camion', 'albaran','conductor','fecharuta'),)

class Mercancia(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=90, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    volumen = models.FloatField(blank=True, null=True)
    fechaentregaaprox = models.DateField(db_column='fechaEntregaAprox')  # Field name made lowercase.
    cliente_dni = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cliente_dni')
    albaran = models.ForeignKey(Albaran, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.descripcion} {self.cliente_dni}'

    class Meta:
        managed = True
        db_table = 'mercancia'

# Calcula el campo pesomercanciamax si se ha dejado en blanco
@receiver(post_save, sender=Camion)
def camion_created_handler(sender, instance, created, *args, **kwargs):
    if created and not instance.pesomercanciamax:
        instance.pesomercanciamax = instance.mma - instance.tara
        instance.save()
    else:
        if not instance.pesomercanciamax:
            instance.pesomercanciamax = instance.mma - instance.tara
            instance.save()
    
    if created and not instance.volumenmercanciamax:
        instance.volumenmercanciamax = instance.largo * instance.ancho * instance.alto
        instance.save()
    else:
        if not instance.volumenmercanciamax:
            instance.volumenmercanciamax = instance.largo * instance.ancho * instance.alto
            instance.save()

@receiver(post_save, sender=Transportista)
def transportista_created_handler(sender, instance, created, *args, **kwargs):
    if created and instance.direccion and not instance.lat and not instance.lon:
        address = instance.direccion + "," + instance.cp + "," + instance.provincia + "," + instance.poblacion
        instance.lat, instance.lon = address_to_coordinates(address)

        instance.save()
    else:
        if instance.direccion and not instance.lat and not instance.lon:
            address = instance.direccion + "," + instance.cp + "," + instance.provincia + "," + instance.poblacion
            instance.lat, instance.lon = address_to_coordinates(address)
            
            instance.save()

@receiver(post_save, sender=Cliente)
def cliente_created_handler(sender, instance, created, *args, **kwargs):
    if created and instance.direccion and not instance.lat and not instance.lon:
        address = instance.direccion + "," + instance.cp + "," + instance.provincia + "," + instance.poblacion
        instance.lat, instance.lon = address_to_coordinates(address)

        instance.save()
    else:
        if instance.direccion and not instance.lat and not instance.lon:
            address = instance.direccion + "," + instance.cp + "," + instance.provincia + "," + instance.poblacion
            instance.lat, instance.lon = address_to_coordinates(address)
            
            instance.save()

@receiver(post_save, sender=Conductor)
def conductor_created_handler(sender, instance, created, *args, **kwargs):
    if created and instance.email and instance.password and not instance.uid_firebase:
        instance.uid_firebase = get_uid_firebase(instance)

        print(instance)
        instance.save()
    else:
        if  instance.email and instance.password and not instance.uid_firebase:
            instance.uid_firebase = get_uid_firebase(instance)
            
            print(instance)
            instance.save()

def get_transportista_id_by_camion_id(camion_id):
    camion = Camion.objects.get(pk=camion_id)
    print(camion.transportista)

    return camion.transportista

@receiver(post_save, sender=Ruta)
def ruta_created_handler(sender, instance, created, *args, **kwargs):
    if created and instance.camion and instance.conductor and instance.fecharuta and instance.transportista == get_transportista_id_by_camion_id(instance.camion.id):
        
        conductor_asigned = ConductoresConducenCamiones(
            camion = instance.camion,
            conductor = instance.conductor,
            fecha = instance.fecharuta
        )

        albaran_asigned = Albaran.objects.get(pk=instance.albaran.id)
        albaran_asigned.estado = Estado.objects.get(pk=2)
        albaran_asigned.save()

        print(conductor_asigned)
        conductor_asigned.save()
    else:
        if created and instance.camion and instance.conductor and instance.fecharuta and instance.transportista == get_transportista_id_by_camion_id(instance.id):
        
            conductor_asigned = ConductoresConducenCamiones(
            camion = instance.camion,
            conductor = instance.conductor,
            fecha = instance.fecharuta
            )

        albaran_asigned = Albaran.objects.get(pk=instance.albaran.id)
        albaran_asigned.estado = Estado.objects.get(pk=2)
        albaran_asigned.save()
        
        print(conductor_asigned)
        conductor_asigned.save()

def address_to_coordinates(address):

    API_KEY = 'AIzaSyBYBUANCXKZevB8vPY2QVKAEFub80JMAKU'

    params = {
        'key': API_KEY,
        'address': address,
        
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params).json()

    if response['status'] == 'OK':
        geometry = response['results'][0]['geometry']
        
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']

        return lat, lon

    else:
        print("Algo fue mal con la API Geocoding de Google Maps.")

def get_uid_firebase(instance):

    cred = {
    # REMOVED FOR PRIVACY
    }

    firebase_admin.initialize_app(credentials.Certificate(cred))

    user = auth.create_user(
        email=instance.email,
        password=instance.password,
        display_name=instance.nombre,
        disabled=False
    )
    print('Sucessfully created new user: {0}'.format(user.uid))

    return user.uid

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=70)
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    
    class Meta:
        # managed = True
        db_table = 'extended_user'

        def __str__(self):
            return self.user.username

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

