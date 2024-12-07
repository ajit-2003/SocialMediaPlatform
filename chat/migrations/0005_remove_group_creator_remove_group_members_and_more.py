# Generated by Django 5.0.7 on 2024-12-07 18:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_message_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.RemoveField(
            model_name='groupmessage',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupmessage',
            name='sender',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='receiver',
            new_name='recipient',
        ),
        migrations.AlterModelTable(
            name='message',
            table=None,
        ),
        migrations.CreateModel(
            name='GroupChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_groups', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='group_members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ConnectionRequest',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='GroupMessage',
        ),
    ]
