# Generated by Django 4.0.4 on 2022-05-31 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0187_remove_mercancia_albaran'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mercancia',
            name='cliente_dni',
        ),
    ]
