# Generated by Django 4.0.4 on 2022-05-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0092_remove_conductor_camiones'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductor',
            name='camiones',
            field=models.ManyToManyField(related_name='Conductores', to='principal.camion'),
        ),
    ]
