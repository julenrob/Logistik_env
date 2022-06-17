# Generated by Django 4.0.4 on 2022-05-16 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_remove_camion_tara_camion_peso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camion',
            name='capacidaddeposito',
        ),
        migrations.RemoveField(
            model_name='camion',
            name='capacidadmercancia',
        ),
        migrations.RemoveField(
            model_name='camion',
            name='peso',
        ),
        migrations.RemoveField(
            model_name='camion',
            name='pesomaxadm',
        ),
        migrations.AddField(
            model_name='camion',
            name='litrosdeposito',
            field=models.FloatField(blank=True, db_column='litrosDeposito', null=True),
        ),
        migrations.AddField(
            model_name='camion',
            name='mma',
            field=models.FloatField(blank=True, db_column='MMA', null=True),
        ),
        migrations.AddField(
            model_name='camion',
            name='pesomercanciamax',
            field=models.FloatField(blank=True, db_column='pesoMercanciaMax', null=True),
        ),
        migrations.AddField(
            model_name='camion',
            name='tara',
            field=models.FloatField(blank=True, db_column='TARA', null=True),
        ),
        migrations.AddField(
            model_name='camion',
            name='volumenmercanciamax',
            field=models.FloatField(blank=True, db_column='volumenMercanciaMax', null=True),
        ),
    ]
