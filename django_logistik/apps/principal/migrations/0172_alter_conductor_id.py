# Generated by Django 4.0.4 on 2022-05-31 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0171_alter_conductor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductor',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
