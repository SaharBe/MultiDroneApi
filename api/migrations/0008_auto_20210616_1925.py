# Generated by Django 3.1.7 on 2021-06-16 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_dronemission'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Command',
            new_name='DroneCommand',
        ),
    ]
