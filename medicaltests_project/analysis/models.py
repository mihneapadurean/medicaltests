from django.db import models
from authentication.models import Patient


class HealthClinic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return (str(self.name))


class MedicalTest(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.PROTECT)
    health_clinic=models.ForeignKey(HealthClinic,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return ("Medical Test having patient "+str(self.patient)+" and clinic as "+str(self.health_clinic)+ "\n")


class ResultType(models.Model):
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    measurementUnit=models.CharField(max_length=200)

    def __str__(self):
        return ("Result type having name: "+str(self.name)+"\nCategory: "+str(self.category)+"\nMeasurement Unit: "+str(self.measurementUnit)+"\n")

class Result(models.Model):
    value=models.FloatField(null=True)
    medicalTest=models.ForeignKey(MedicalTest,on_delete=models.PROTECT, related_name="results")
    resultType=models.ForeignKey(ResultType,on_delete=models.PROTECT)

    def __str__(self):
        return ("Result:\n"+"Value: "+str(self.value)+"\n"+str(self.medicalTest)+str(self.resultType))


