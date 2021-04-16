# Generated by Django 3.1.7 on 2021-03-31 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drone',
            name='name',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='drone',
            name='connect',
            field=models.BooleanField(),
        ),
    ]
