# Generated by Django 5.0.7 on 2024-10-03 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='message',
            table='chatmessage',
        ),
    ]
