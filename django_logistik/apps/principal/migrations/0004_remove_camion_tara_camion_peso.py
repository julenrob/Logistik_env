# Generated by Django 4.0.4 on 2022-05-16 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_remove_camion_litrosdeposito_remove_camion_mma_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camion',
            name='tara',
        ),
        migrations.AddField(
            model_name='camion',
            name='peso',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]