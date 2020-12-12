from .models import *
from authentication.models import Patient,Gender,User
import datetime

def populateList():
    for i in range(0,10):
        user=User(username="username"+str(i),password="pass"+str(i),email="email"+str(i)+"@gmail.com",city="city"+str(i),birth_day="2000-01-"+str(i+1),gender=Gender.objects.get(pk=i%2+1))
        user.save()
        newPatient=Patient(User=user,weight=(i+1)*10)
        newPatient.save()
        hc=HealthClinic(name="clinic"+str(i))
        mt=MedicalTest(patient=newPatient,health_clinic=hc)
        rt=ResultType(name="rt"+str(i),category="c"+str(i),measurementUnit="mu"+str(i))
        res=Result(value=float(i),medicalTest=mt,resultType=rt)
        hc.save()
        mt.save()
        rt.save()
        res.save()


def someFunction():
    user=User.objects.get(username="mihneapadurean")
    newPatient=Patient(User=user,weight=75)
    newPatient.save()
    for i in range(11,16):
        hc=HealthClinic(name="clinic"+str(i))
        mt=MedicalTest(patient=newPatient,health_clinic=hc)
        rt=ResultType(name="rt"+str(i),category="c"+str(i),measurementUnit="mu"+str(i))
        res=Result(value=float(i),medicalTest=mt,resultType=rt)
        hc.save()
        mt.save()
        rt.save()
        res.save()


def deleteAll():
    for i in range(10):
        Result.objects.get(pk=i+1).delete()

populateList()
someFunction()