# Generated by Django 4.0.4 on 2022-06-11 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0260_alter_ruta_transportista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='albaran',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albaran_id', to='principal.albaran'),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='camion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camion_id', to='principal.camion'),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='conductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conductor_id', to='principal.conductor'),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='transportista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transportista_id', to='principal.transportista'),
        ),
    ]
