# Generated by Django 2.1.2 on 2018-11-12 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20181112_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='authors',
            field=models.ManyToManyField(to='base.Author'),
        ),
    ]
