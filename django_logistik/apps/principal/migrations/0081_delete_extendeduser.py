# Generated by Django 4.0.4 on 2022-05-28 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0080_remove_extendeduser_transportista'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExtendedUser',
        ),
    ]