# Generated by Django 5.1.5 on 2025-02-27 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0034_remove_unregisteredcolleges_clg_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='universityincharge',
            name='trimmed_university_name',
        ),
        migrations.AlterField(
            model_name='universityincharge',
            name='clg_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
