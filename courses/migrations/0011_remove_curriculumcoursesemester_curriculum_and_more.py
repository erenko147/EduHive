# Generated by Django 5.1.1 on 2024-10-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_remove_course_is_it_offered_curriculumcoursesemester_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculumcoursesemester',
            name='curriculum',
        ),
        migrations.AddField(
            model_name='curriculumcoursesemester',
            name='program_code',
            field=models.CharField(default='CENG', max_length=100),
        ),
        migrations.AddField(
            model_name='curriculumcoursesemester',
            name='program_name',
            field=models.CharField(default='Computer science', max_length=200),
        ),
    ]
