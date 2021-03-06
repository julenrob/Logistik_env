# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Albaran(models.Model):
    fechaentrega = models.DateField(db_column='fechaEntrega')  # Field name made lowercase.
    horamin = models.TimeField(db_column='horaMin')  # Field name made lowercase.
    horamax = models.TimeField(db_column='horaMax')  # Field name made lowercase.
    cliente_dni = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente_dni')
    estado = models.ForeignKey('Estado', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'albaran'


class Asigna(models.Model):
    transportista = models.OneToOneField('Transportista', models.DO_NOTHING, primary_key=True)
    camion = models.ForeignKey('Camion', models.DO_NOTHING)
    albaran = models.ForeignKey(Albaran, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'asigna'
        unique_together = (('transportista', 'albaran'), ('albaran', 'camion'),)


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


class Camion(models.Model):
    marca = models.CharField(max_length=45, blank=True, null=True)
    tara = models.FloatField(db_column='TARA', blank=True, null=True)  # Field name made lowercase.
    mma = models.FloatField(db_column='MMA', blank=True, null=True)  # Field name made lowercase.
    pesomercanciamax = models.FloatField(db_column='pesoMercanciaMax', blank=True, null=True)  # Field name made lowercase.
    volumenmercanciamax = models.FloatField(db_column='volumenMercanciaMax', blank=True, null=True)  # Field name made lowercase.
    litrosdeposito = models.FloatField(db_column='litrosDeposito', blank=True, null=True)  # Field name made lowercase.
    matricula = models.CharField(max_length=20, blank=True, null=True)
    kilometros = models.FloatField(blank=True, null=True)
    transportista = models.ForeignKey('Transportista', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'camion'


class Cliente(models.Model):
    dni = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=45)
    apellido1 = models.CharField(max_length=45)
    apellido2 = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45)
    provincia = models.CharField(max_length=45)
    poblacion = models.CharField(max_length=45)
    cp = models.IntegerField()
    movil = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Conductor(models.Model):
    nombre = models.CharField(max_length=45)
    apellido1 = models.CharField(max_length=45, blank=True, null=True)
    apellido2 = models.CharField(max_length=45, blank=True, null=True)
    camion = models.ForeignKey(Camion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'conductor'


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


class Estado(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class Mercancia(models.Model):
    descripcion = models.CharField(max_length=90)
    peso = models.FloatField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    volumen = models.FloatField(blank=True, null=True)
    fechaentregaaprox = models.DateField(db_column='fechaEntregaAprox')  # Field name made lowercase.
    cliente_dni = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_dni')
    albaran = models.ForeignKey(Albaran, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mercancia'


class Transportista(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45)
    provincia = models.CharField(max_length=45)
    poblacion = models.CharField(max_length=45)
    cp = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'transportista'


class Usuario(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    rol = models.CharField(max_length=45, blank=True, null=True)
    transportista = models.ForeignKey(Transportista, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario'
