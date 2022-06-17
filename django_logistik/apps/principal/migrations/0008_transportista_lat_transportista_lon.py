# Generated by Django 4.0.4 on 2022-05-24 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_alter_transportista_provincia'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportista',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='transportista',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]