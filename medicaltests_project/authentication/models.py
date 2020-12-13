from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Gender(models.Model): #Male or Female
    name = models.CharField('name', max_length=10)

class User(AbstractUser):
    email = models.EmailField('email', max_length=100, null=False, unique=True)
    city = models.CharField('city', max_length=30)
    birth_day = models.DateField('birthDay')
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)

class Medic(models.Model):
    user = models.ForeignKey(User, related_name="medic_info", on_delete=models.PROTECT)
    hospital = models.CharField('hospital', max_length=30)

class Patient(models.Model):
    user = models.ForeignKey(User, related_name="patient_info", on_delete=models.PROTECT)
    weight = models.IntegerField('weight')