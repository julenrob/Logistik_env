# Generated by Django 4.0.4 on 2022-06-05 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0216_ruta_fecharuta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albaran',
            options={'managed': True, 'verbose_name_plural': 'Albaranes'},
        ),
        migrations.AlterModelOptions(
            name='camion',
            options={'managed': True, 'verbose_name_plural': 'Camiones'},
        ),
        migrations.AlterModelOptions(
            name='conductor',
            options={'managed': True, 'verbose_name_plural': 'Conductores'},
        ),
        migrations.AlterModelOptions(
            name='conductoresconducencamiones',
            options={'managed': True, 'verbose_name_plural': 'Conductores conducen Camiones'},
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='telefono',
            field=models.CharField(default='123456789', max_length=70),
        ),
    ]
