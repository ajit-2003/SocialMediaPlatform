# Generated by Django 5.0.7 on 2024-10-03 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='profile',
            table='accounts_profile',
        ),
    ]
