# Generated by Django 4.0.4 on 2022-05-31 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0210_alter_conductoresconducencamiones_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albaran',
            name='cliente_dni',
            field=models.ForeignKey(db_column='cliente_dni', default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.cliente'),
        ),
        migrations.AlterField(
            model_name='albaran',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.estado'),
        ),
        migrations.AlterField(
            model_name='camion',
            name='transportista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.transportista'),
        ),
        migrations.AlterField(
            model_name='conductoresconducencamiones',
            name='camion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.camion'),
        ),
        migrations.AlterField(
            model_name='conductoresconducencamiones',
            name='conductor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.conductor'),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='transportista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.transportista'),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mercancia',
            name='albaran',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.albaran'),
        ),
        migrations.AlterField(
            model_name='mercancia',
            name='cliente_dni',
            field=models.ForeignKey(db_column='cliente_dni', default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.cliente'),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='albaran',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.albaran'),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='camion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.camion'),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='transportista',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='principal.transportista'),
        ),
    ]
