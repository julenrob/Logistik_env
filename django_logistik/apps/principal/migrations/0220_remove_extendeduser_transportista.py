# Generated by Django 4.0.4 on 2022-06-05 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0219_extendeduser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='transportista',
        ),
    ]
