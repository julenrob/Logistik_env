# Generated by Django 4.0.4 on 2022-05-31 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0206_remove_extendeduser_movil'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConductorConduceCamiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('camion', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.camion')),
                ('conductor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.conductor')),
            ],
            options={
                'db_table': 'conductorconducecamiones',
                'managed': True,
                'unique_together': {('camion', 'conductor', 'fecha')},
            },
        ),
    ]