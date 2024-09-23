# Generated by Django 5.1.1 on 2024-09-23 11:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='chatroom.room'),
            preserve_default=False,
        ),
    ]