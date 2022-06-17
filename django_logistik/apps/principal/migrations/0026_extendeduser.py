# Generated by Django 4.0.4 on 2022-05-27 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0025_delete_extendeduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transportista', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.transportista')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.authuser')),
            ],
            options={
                'db_table': 'extended_user',
                'managed': True,
            },
        ),
    ]
