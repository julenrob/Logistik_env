# Generated by Django 4.0.4 on 2022-05-26 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0012_alter_conductor_nombre_alter_estado_nombre_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
