# Generated by Django 4.2.11 on 2024-07-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0003_job_questions_alter_company_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('summary', models.TextField()),
                ('experience', models.TextField()),
                ('education', models.TextField()),
                ('skills', models.TextField()),
            ],
        ),
    ]
