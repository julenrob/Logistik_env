# Generated by Django 4.0.4 on 2022-06-06 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0236_alter_ruta_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='id',
            field=models.BigAutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='transportista',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='principal.transportista'),
        ),
    ]