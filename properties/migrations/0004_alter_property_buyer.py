# Generated by Django 4.1.2 on 2022-10-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0003_alter_property_buyer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="buyer",
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
