# Generated by Django 4.1.2 on 2022-10-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Property",
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
                ("property_name", models.CharField(max_length=255)),
                ("owner_name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("landmark", models.CharField(max_length=255)),
                ("pincode", models.IntegerField(max_length=6)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("property_type", models.CharField(max_length=255)),
            ],
        ),
    ]
