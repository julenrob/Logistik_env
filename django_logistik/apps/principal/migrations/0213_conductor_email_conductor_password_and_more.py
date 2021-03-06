# Generated by Django 4.0.4 on 2022-06-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0212_conductor_uid_firebase'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductor',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=40),
        ),
        migrations.AddField(
            model_name='conductor',
            name='password',
            field=models.CharField(default='password', max_length=40),
        ),
        migrations.AddField(
            model_name='conductor',
            name='telefono',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
