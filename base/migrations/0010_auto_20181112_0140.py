# Generated by Django 2.1.2 on 2018-11-12 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_resource_areas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.URLField(max_length=500, unique=True),
        ),
    ]
