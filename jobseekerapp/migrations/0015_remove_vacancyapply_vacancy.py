# Generated by Django 3.0.2 on 2020-03-04 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseekerapp', '0014_auto_20200303_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancyapply',
            name='vacancy',
        ),
    ]