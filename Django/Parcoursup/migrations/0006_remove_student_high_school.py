# Generated by Django 5.1.1 on 2024-10-23 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parcoursup', '0005_student_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='high_school',
        ),
    ]