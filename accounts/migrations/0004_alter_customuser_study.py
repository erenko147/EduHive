# Generated by Django 5.1 on 2024-09-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_student_number_delete_academicdream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='study',
            field=models.CharField(blank=True, choices=[('CENG', 'Computer Science'), ('ENG', 'Engineering'), ('BIO', 'Biology')], max_length=50, null=True),
        ),
    ]