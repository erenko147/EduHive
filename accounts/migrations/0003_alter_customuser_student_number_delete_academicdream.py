# Generated by Django 5.1 on 2024-08-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_student_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='student_number',
            field=models.CharField(blank=True, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='AcademicDream',
        ),
    ]