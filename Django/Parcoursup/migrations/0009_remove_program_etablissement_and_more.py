# Generated by Django 5.1.1 on 2024-10-23 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parcoursup', '0008_alter_offer_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='etablissement',
        ),
        migrations.RemoveField(
            model_name='application',
            name='program',
        ),
        migrations.RemoveField(
            model_name='etablissement',
            name='name',
        ),
        migrations.AddField(
            model_name='application',
            name='offer',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Parcoursup.offer'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OfferPro',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
    ]