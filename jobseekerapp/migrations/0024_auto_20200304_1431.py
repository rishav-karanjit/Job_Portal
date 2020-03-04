# Generated by Django 3.0.2 on 2020-03-04 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiterapp', '0003_remove_vacancy_applied_user'),
        ('jobseekerapp', '0023_auto_20200304_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancyapply',
            name='vacancy',
        ),
        migrations.AddField(
            model_name='vacancyapply',
            name='vacancy',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='recruiterapp.Vacancy'),
            preserve_default=False,
        ),
    ]