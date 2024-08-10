# Generated by Django 5.1 on 2024-08-10 21:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=10, unique=True, verbose_name='License Plate')),
                ('brand', models.CharField(max_length=20, verbose_name='Brand')),
                ('color', models.CharField(max_length=15, verbose_name='Color')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='persons.person')),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles',
            },
        ),
    ]
