# Generated by Django 3.1.7 on 2021-04-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210401_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='drone_name',
        ),
        migrations.AddField(
            model_name='command',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='command',
            name='command',
            field=models.CharField(default='', max_length=20),
        ),
    ]