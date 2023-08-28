# Generated by Django 4.2.1 on 2023-08-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                    "address",
                    models.CharField(max_length=100, verbose_name="Street address"),
                ),
                (
                    "address_detail",
                    models.CharField(
                        max_length=100,
                        verbose_name="Apartment, Suite, Unit, Box number, etc.",
                    ),
                ),
                (
                    "locality",
                    models.CharField(max_length=100, verbose_name="City or Town name"),
                ),
                (
                    "administrative_area",
                    models.CharField(
                        max_length=50, verbose_name="State, Province or Region name"
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        default="NG",
                        max_length=2,
                        verbose_name="Country 2 character ISO code. Defaults to NG",
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(max_length=10, verbose_name="Postal code"),
                ),
                (
                    "osm_checked",
                    models.BooleanField(verbose_name="Checked by Open Street Map API"),
                ),
                ("osm_longitude", models.FloatField()),
                ("osm_latitude", models.FloatField()),
            ],
        ),
    ]
