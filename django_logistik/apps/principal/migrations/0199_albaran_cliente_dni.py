# Generated by Django 4.0.4 on 2022-05-31 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0198_camion_transportista'),
    ]

    operations = [
        migrations.AddField(
            model_name='albaran',
            name='cliente_dni',
            field=models.ForeignKey(db_column='cliente_dni', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.cliente'),
        ),
    ]
