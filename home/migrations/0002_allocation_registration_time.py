# Generated by Django 5.0.10 on 2024-12-26 11:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="allocation",
            name="registration_time",
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                help_text="This contains the date and time of registration",
                null=True,
                verbose_name="Registration time",
            ),
        ),
    ]
