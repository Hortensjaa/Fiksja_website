# Generated by Django 4.1.1 on 2022-09-24 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_remove_break_break_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='break',
            name='break_date',
            field=models.DateField(default=datetime.date(1997, 10, 19)),
        ),
    ]