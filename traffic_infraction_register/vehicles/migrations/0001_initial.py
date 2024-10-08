# Generated by Django 5.1 on 2024-08-11 01:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("persons", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "license_plate",
                    models.CharField(
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="License Plate",
                    ),
                ),
                ("brand", models.CharField(max_length=20, verbose_name="Brand")),
                ("color", models.CharField(max_length=15, verbose_name="Color")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicles",
                        to="persons.person",
                    ),
                ),
            ],
            options={
                "verbose_name": "Vehicle",
                "verbose_name_plural": "Vehicles",
            },
        ),
    ]
