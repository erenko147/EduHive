# Generated by Django 5.1.1 on 2024-10-03 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_rename_curriculumcoursesemester_academicdream_curriculum_course_semester'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AcademicDream',
        ),
    ]
