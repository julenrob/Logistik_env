# Generated by Django 4.0.4 on 2022-05-31 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0154_extendeduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'test',
                'managed': True,
            },
        ),
    ]
