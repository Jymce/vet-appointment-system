# Generated by Django 5.2.1 on 2025-05-31 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_alter_groomingappointment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groomingappointment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Canceled', 'Canceled')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='veterinaryappointment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Canceled', 'Canceled')], default='Pending', max_length=10),
        ),
    ]
