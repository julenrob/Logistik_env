# Generated by Django 4.0.4 on 2022-05-30 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0137_remove_extendeduser_transportista'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='transportista',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.transportista'),
        ),
    ]
