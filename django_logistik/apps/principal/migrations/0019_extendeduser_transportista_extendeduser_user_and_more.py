# Generated by Django 4.0.4 on 2022-05-27 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0018_alter_extendeduser_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='transportista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.transportista'),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.authuser'),
        ),
        migrations.AlterModelTable(
            name='extendeduser',
            table=None,
        ),
    ]
