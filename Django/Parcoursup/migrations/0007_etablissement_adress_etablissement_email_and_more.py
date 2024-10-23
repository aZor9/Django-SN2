# Generated by Django 5.1.1 on 2024-10-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parcoursup', '0006_remove_student_high_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='etablissement',
            name='adress',
            field=models.CharField(default='adress', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etablissement',
            name='email',
            field=models.EmailField(default='mail@mail.com', max_length=127, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etablissement',
            name='study_domain',
            field=models.CharField(choices=[('science', 'Science'), ('literature', 'Literature'), ('engineering', 'Engineering'), ('arts', 'Arts'), ('business', 'Business'), ('medicine', 'Medicine')], default='science', max_length=50),
        ),
    ]
