# Generated by Django 5.1.1 on 2024-10-23 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parcoursup', '0007_etablissement_adress_etablissement_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Parcoursup.etablissement'),
        ),
    ]
