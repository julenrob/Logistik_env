# Generated by Django 4.0.4 on 2022-05-29 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0102_remove_conductor_conducido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConductorConduceCamion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.camion')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='conductor',
            name='conducido',
            field=models.ManyToManyField(through='principal.ConductorConduceCamion', to='principal.camion'),
        ),
        migrations.AddField(
            model_name='conductorconducecamion',
            name='conductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.conductor'),
        ),
        migrations.AlterUniqueTogether(
            name='conductorconducecamion',
            unique_together={('camion', 'conductor', 'fecha')},
        ),
    ]
