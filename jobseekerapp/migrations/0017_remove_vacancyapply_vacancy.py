# Generated by Django 3.0.2 on 2020-03-04 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseekerapp', '0016_vacancyapply_vacancy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancyapply',
            name='vacancy',
        ),
    ]