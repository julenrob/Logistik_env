# Generated by Django 4.0.4 on 2022-05-16 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaentrega', models.DateField(db_column='fechaEntrega')),
                ('horamin', models.TimeField(db_column='horaMin')),
                ('horamax', models.TimeField(db_column='horaMax')),
            ],
            options={
                'db_table': 'albaran',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(blank=True, max_length=45, null=True)),
                ('peso', models.CharField(blank=True, max_length=45, null=True)),
                ('pesomaxadm', models.FloatField(blank=True, db_column='pesoMaxAdm', null=True)),
                ('capacidaddeposito', models.FloatField(blank=True, db_column='capacidadDeposito', null=True)),
                ('matricula', models.CharField(blank=True, max_length=20, null=True)),
                ('kilometros', models.FloatField(blank=True, null=True)),
                ('capacidadmercancia', models.FloatField(blank=True, db_column='capacidadMercancia', null=True)),
            ],
            options={
                'db_table': 'camion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('dni', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido1', models.CharField(max_length=45)),
                ('apellido2', models.CharField(blank=True, max_length=45, null=True)),
                ('direccion', models.CharField(max_length=45)),
                ('provincia', models.CharField(max_length=45)),
                ('poblacion', models.CharField(max_length=45)),
                ('cp', models.IntegerField()),
                ('movil', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('descripcion', models.CharField(blank=True, max_length=90, null=True)),
            ],
            options={
                'db_table': 'estado',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transportista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('direccion', models.CharField(max_length=45)),
                ('provincia', models.CharField(max_length=45)),
                ('poblacion', models.CharField(max_length=45)),
                ('cp', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'transportista',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('rol', models.CharField(blank=True, max_length=45, null=True)),
                ('transportista', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.transportista')),
            ],
            options={
                'db_table': 'usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mercancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=90)),
                ('peso', models.FloatField(blank=True, null=True)),
                ('cantidad', models.FloatField(blank=True, null=True)),
                ('volumen', models.FloatField(blank=True, null=True)),
                ('fechaentregaaprox', models.DateField(db_column='fechaEntregaAprox')),
                ('albaran', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.albaran')),
                ('cliente_dni', models.ForeignKey(db_column='cliente_dni', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.cliente')),
            ],
            options={
                'db_table': 'mercancia',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido1', models.CharField(blank=True, max_length=45, null=True)),
                ('apellido2', models.CharField(blank=True, max_length=45, null=True)),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.camion')),
            ],
            options={
                'db_table': 'conductor',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='camion',
            name='transportista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.transportista'),
        ),
        migrations.AddField(
            model_name='albaran',
            name='cliente_dni',
            field=models.ForeignKey(db_column='cliente_dni', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.cliente'),
        ),
        migrations.AddField(
            model_name='albaran',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.estado'),
        ),
        migrations.CreateModel(
            name='Asigna',
            fields=[
                ('transportista', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='principal.transportista')),
                ('albaran', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.albaran')),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.camion')),
            ],
            options={
                'db_table': 'asigna',
                'managed': True,
                'unique_together': {('albaran', 'camion'), ('transportista', 'albaran')},
            },
        ),
    ]