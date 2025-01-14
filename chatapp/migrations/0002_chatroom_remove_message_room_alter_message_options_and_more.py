# Generated by Django 5.0.6 on 2024-08-04 09:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='body',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='created',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='message',
            name='updated',
        ),
        migrations.AddField(
            model_name='message',
            name='chat_room',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chatapp.chatroom'),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('chat_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.chatroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
