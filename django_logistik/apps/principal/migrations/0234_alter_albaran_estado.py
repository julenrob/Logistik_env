# Generated by Django 4.0.4 on 2022-06-05 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0233_alter_extendeduser_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albaran',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.estado'),
        ),
    ]
