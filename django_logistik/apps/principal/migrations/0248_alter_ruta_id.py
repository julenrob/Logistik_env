# Generated by Django 4.0.4 on 2022-06-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0247_ruta_id_alter_ruta_transportista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
