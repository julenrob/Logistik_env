# Generated by Django 4.0.4 on 2022-05-28 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0056_extendeduser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExtendedUser',
        ),
    ]