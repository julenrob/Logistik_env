# Generated by Django 4.0.4 on 2022-06-05 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0220_remove_extendeduser_transportista'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='transportista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.transportista'),
        ),
    ]
