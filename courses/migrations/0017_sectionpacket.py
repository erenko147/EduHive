# Generated by Django 5.1.1 on 2024-10-03 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_academicdream'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionPacket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.section')),
            ],
        ),
    ]