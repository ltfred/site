# Generated by Django 2.2.13 on 2021-02-23 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photocategory',
            options={'ordering': ['-created_at'], 'verbose_name': '照片分类', 'verbose_name_plural': '照片分类'},
        ),
    ]
