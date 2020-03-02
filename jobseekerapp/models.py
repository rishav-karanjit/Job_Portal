from django.db import models
from Jobapp.models import *
from recruiterapp.models import *
from .choices import *
class VacancyApply(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    vacancy=models.ForeignKey(Vacancy,on_delete=models.CASCADE)
    applieddate=models.DateField(auto_now=True)
    status=models.IntegerField(choices=status_choices,default=1)
# Create your models here.
