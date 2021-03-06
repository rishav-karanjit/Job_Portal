# Generated by Django 3.0.2 on 2020-04-22 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruiterapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JseekerEdu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('field_of_study', models.CharField(max_length=50)),
                ('date_started', models.DateField(blank=True, null=True)),
                ('date_ended', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applieddate', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Selected'), (3, 'Rejected')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vac', to='recruiterapp.Vacancy')),
            ],
        ),
        migrations.CreateModel(
            name='JseekerSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JseekerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appliedvacancy', models.ManyToManyField(to='jobseekerapp.VacancyApply')),
                ('education', models.ManyToManyField(to='jobseekerapp.JseekerEdu')),
                ('skills', models.ManyToManyField(to='jobseekerapp.JseekerSkill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
