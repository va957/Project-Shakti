# Generated by Django 3.2.5 on 2022-06-25 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20220625_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('temperature', models.PositiveSmallIntegerField(null=True)),
                ('high_bp', models.PositiveSmallIntegerField(null=True)),
                ('low_bp', models.PositiveSmallIntegerField(null=True)),
                ('pulse', models.PositiveSmallIntegerField(null=True)),
                ('respiration', models.PositiveSmallIntegerField(null=True)),
                ('oxygen_saturation', models.PositiveSmallIntegerField(null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.patient')),
                ('rmp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.rmp')),
            ],
        ),
    ]
