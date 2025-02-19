# Generated by Django 5.0.7 on 2024-11-06 05:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('Code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Currency', models.CharField(max_length=25)),
                ('IsActive', models.BooleanField(default=True, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('Code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Country', models.CharField(max_length=25)),
                ('IsActive', models.BooleanField(default=True, max_length=1)),
                ('Currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.currency')),
            ],
        ),
    ]
