# Generated by Django 4.0.4 on 2022-05-24 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0010_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=50),
        ),
    ]
