# Generated by Django 5.0.7 on 2024-10-03 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='message',
            table='chat_message',
        ),
    ]