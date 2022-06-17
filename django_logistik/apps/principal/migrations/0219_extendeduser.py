# Generated by Django 4.0.4 on 2022-06-05 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0218_delete_extendeduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(default='123456789', max_length=70)),
                ('transportista', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.transportista')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'extended_user',
                'managed': True,
            },
        ),
    ]
