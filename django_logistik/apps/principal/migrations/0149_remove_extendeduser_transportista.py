# Generated by Django 4.0.4 on 2022-05-30 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0148_extendeduser_transportista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='transportista',
        ),
    ]
