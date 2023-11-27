# Generated by Django 4.1.7 on 2023-11-25 14:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("RestotelMap", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appartenir",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Service",
            },
        ),
        migrations.CreateModel(
            name="Catego",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "libelle",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Libellé"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Catégories",
            },
        ),
        migrations.CreateModel(
            name="Etabl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100, verbose_name="Nom")),
                (
                    "telephone",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Téléphone"
                    ),
                ),
                ("latitude", models.FloatField(verbose_name="Latitude")),
                ("longitude", models.FloatField(verbose_name="Longitude")),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPointField(srid=4326),
                ),
                (
                    "catego",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="RestotelMap.catego",
                        verbose_name="Catégorie",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Etablissement",
            },
        ),
        migrations.CreateModel(
            name="Local",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ville",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        unique=True,
                        verbose_name="Ville",
                    ),
                ),
                (
                    "commune",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Commune"
                    ),
                ),
                (
                    "quartier",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Quartier"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Localisation",
            },
        ),
        migrations.RemoveField(
            model_name="etablissement",
            name="categorie",
        ),
        migrations.RemoveField(
            model_name="etablissement",
            name="situa_geo",
        ),
        migrations.DeleteModel(
            name="Categorie",
        ),
        migrations.DeleteModel(
            name="Etablissement",
        ),
        migrations.DeleteModel(
            name="Localisation",
        ),
        migrations.AddField(
            model_name="etabl",
            name="local",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="RestotelMap.local",
                verbose_name="Localisation",
            ),
        ),
        migrations.AddField(
            model_name="appartenir",
            name="catego",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="RestotelMap.catego",
                verbose_name="Catégorie",
            ),
        ),
        migrations.AddField(
            model_name="appartenir",
            name="etab",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="RestotelMap.etabl",
                verbose_name="Etablissement",
            ),
        ),
    ]