# Generated by Django 4.0.4 on 2022-06-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0239_alter_ruta_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
