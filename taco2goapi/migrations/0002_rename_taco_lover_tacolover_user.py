# Generated by Django 4.1 on 2022-09-10 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taco2goapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tacolover',
            old_name='taco_lover',
            new_name='user',
        ),
    ]