# Generated by Django 4.0.4 on 2022-05-27 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0016_alter_authuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authuser',
            options={'managed': False},
        ),
    ]
