# Generated by Django 4.0.4 on 2022-06-04 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0214_alter_mercancia_albaran'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercancia',
            name='albaran',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.albaran'),
        ),
    ]
