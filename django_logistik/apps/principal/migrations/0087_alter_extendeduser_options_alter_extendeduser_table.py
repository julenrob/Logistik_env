# Generated by Django 4.0.4 on 2022-05-28 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0086_alter_extendeduser_options_alter_extendeduser_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extendeduser',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='extendeduser',
            table='extended_user',
        ),
    ]
