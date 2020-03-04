# Generated by Django 3.0.2 on 2020-03-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiterapp', '0003_remove_vacancy_applied_user'),
        ('jobseekerapp', '0022_vacancyapply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancyapply',
            name='vacancy',
        ),
        migrations.AddField(
            model_name='vacancyapply',
            name='vacancy',
            field=models.ManyToManyField(to='recruiterapp.Vacancy'),
        ),
    ]