# Generated by Django 5.1.1 on 2024-10-18 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parcoursup', '0004_student_firstname_student_study_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='hugo.lembrez@gmail.com', max_length=127, unique=True),
            preserve_default=False,
        ),
    ]
