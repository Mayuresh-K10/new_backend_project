# Generated by Django 4.2.11 on 2024-07-28 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_series', '0002_proctoringsession_session_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proctoringsession',
            name='session_id',
        ),
    ]
