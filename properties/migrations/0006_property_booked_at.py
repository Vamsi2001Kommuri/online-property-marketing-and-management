# Generated by Django 4.1.2 on 2022-10-08 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0005_property_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="booked_at",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]