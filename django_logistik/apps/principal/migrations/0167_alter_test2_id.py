# Generated by Django 4.0.4 on 2022-05-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0166_alter_test2_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test2',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
