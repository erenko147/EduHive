# Generated by Django 5.1 on 2024-09-03 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_academicdream_grade_curriculum_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculum',
            name='required_credits',
        ),
    ]