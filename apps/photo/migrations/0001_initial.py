# Generated by Django 2.2.13 on 2020-12-21 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PhotoCategory",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, verbose_name="名称")),
                ("description", models.CharField(max_length=100, verbose_name="相册描述")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, verbose_name="名称")),
                ("description", models.CharField(max_length=100, verbose_name="描述")),
                ("url", models.URLField(verbose_name="照片地址")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="photo.PhotoCategory", verbose_name="分类"
                    ),
                ),
            ],
            options={
                "verbose_name": "照片",
                "verbose_name_plural": "照片",
                "ordering": ["-created_at"],
            },
        ),
    ]
