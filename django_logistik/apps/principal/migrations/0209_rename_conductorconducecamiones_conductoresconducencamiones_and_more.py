# Generated by Django 4.0.4 on 2022-05-31 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0208_conductor_conducido'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConductorConduceCamiones',
            new_name='ConductoresConducenCamiones',
        ),
        migrations.AlterModelTable(
            name='conductoresconducencamiones',
            table='conductoresconducencamiones',
        ),
    ]
