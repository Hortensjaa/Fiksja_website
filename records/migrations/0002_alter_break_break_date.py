# Generated by Django 4.1.1 on 2022-09-24 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='break',
            name='break_date',
            field=models.DateField(),
        ),
    ]
