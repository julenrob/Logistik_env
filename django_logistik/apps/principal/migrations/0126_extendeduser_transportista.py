# Generated by Django 4.0.4 on 2022-05-30 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0125_remove_extendeduser_transportista'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='transportista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.transportista'),
        ),
    ]
