# Generated by Django 4.0.4 on 2022-06-11 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0259_alter_ruta_transportista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='transportista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.transportista'),
        ),
    ]
