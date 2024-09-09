# Generated by Django 5.1 on 2024-09-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_curriculum_program_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculum',
            name='semester',
        ),
        migrations.AddField(
            model_name='curriculum',
            name='semester',
            field=models.ManyToManyField(related_name='curricula', to='courses.semester'),
        ),
    ]
