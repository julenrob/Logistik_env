# Generated by Django 4.0.4 on 2022-06-06 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0242_alter_ruta_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruta',
            name='id',
        ),
        migrations.AlterField(
            model_name='ruta',
            name='transportista',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='principal.transportista'),
        ),
    ]
