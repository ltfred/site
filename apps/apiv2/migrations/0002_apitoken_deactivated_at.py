# Generated by Django 2.2.13 on 2020-10-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apiv2", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="apitoken",
            name="deactivated_at",
            field=models.DateTimeField(null=True),
        ),
    ]
