# Generated by Django 4.1.1 on 2022-09-24 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('AL', 'Picie alkoholu w wybitny sposób'), ('AT', 'Sprawność i tężyzna fizyczna'), ('M', 'Silna psycha'), ('DR', 'Osiągnięcia związane z innymi używkami'), ('G', 'Ośmieszanie się'), ('DE', 'Niszczenie'), ('O', 'Wszystko inne')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Break',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='0', max_length=200)),
                ('breaker', models.CharField(max_length=50)),
                ('break_date', models.DateTimeField()),
                ('breaker_login', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='records.record')),
            ],
        ),
    ]
