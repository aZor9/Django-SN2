# Generated by Django 5.1.1 on 2024-11-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parcoursup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('student', 'Étudiant'), ('etablissement', 'Établissement'), ('admin', 'Admin')], max_length=20),
        ),
    ]