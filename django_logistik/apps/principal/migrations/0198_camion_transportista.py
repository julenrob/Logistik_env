# Generated by Django 4.0.4 on 2022-05-31 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0197_alter_camion_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='camion',
            name='transportista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.transportista'),
        ),
    ]
