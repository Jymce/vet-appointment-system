# Generated by Django 5.2.1 on 2025-05-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_groomingappointment_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groomingappointment',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='veterinaryappointment',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
