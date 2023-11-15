# Generated by Django 4.0.7 on 2023-11-15 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('temperature', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('zipcode', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]