# Generated by Django 4.2.15 on 2024-09-20 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0051_job_first_name_job_last_name_job_with_promoting_job_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='with_promoting_job',
            new_name='promoting_job',
        ),
        migrations.RemoveField(
            model_name='job',
            name='without_promoting_job',
        ),
    ]
