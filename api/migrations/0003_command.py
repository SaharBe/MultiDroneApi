# Generated by Django 3.1.7 on 2021-04-01 13:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210331_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=20)),
                ('alt', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('drone_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.drone')),
            ],
        ),
    ]
