# Generated by Django 5.1.1 on 2024-10-03 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_academicdream_curriculumcoursesemester_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academicdream',
            old_name='CurriculumCourseSemester',
            new_name='curriculum_course_semester',
        ),
    ]