# Generated by Django 4.0.4 on 2022-05-16 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_remove_camion_capacidaddeposito_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camion',
            name='litrosdeposito',
        ),
        migrations.RemoveField(
            model_name='camion',
            name='mma',
        ),
        migrations.RemoveField(
            model_name='camion',
            name='pesomercanciamax',
        ),
        migrations.RemoveField(
            model_name='camion',
            name='volumenmercanciamax',
        ),
        migrations.AddField(
            model_name='camion',
            name='capacidaddeposito',
            field=models.FloatField(blank=True, db_column='capacidadDeposito', null=True),
        ),
        migrations.AddField(
            model_name='camion',
            name='capacidadmercancia',
            field=models.FloatField(blank=True, db_column='capacidadMercancia', null=True),
        ),
        migrations.AddField(
            model_name='camion',
            name='pesomaxadm',
            field=models.FloatField(blank=True, db_column='pesoMaxAdm', null=True),
        ),
    ]