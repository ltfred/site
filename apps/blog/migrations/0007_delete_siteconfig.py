# Generated by Django 2.2.13 on 2021-02-23 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_friendlink_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SiteConfig',
        ),
    ]
