from django.db import models

class MedicalTest(models.Model):
    patientID=models.BigIntegerField(null=True)

    def __str__(self):
        return ("Medical Test having patientID equal to "+str(self.patientID)+"\n")


class ResultType(models.Model):
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    measurementUnit=models.CharField(max_length=200)

    def __str__(self):
        return ("Result type having name: "+str(self.name)+"\nCategory: "+str(self.category)+"\nMeasurement Unit: "+str(self.measurementUnit)+"\n")

class Result(models.Model):
    value=models.FloatField(null=True)
    medicalTest=models.ForeignKey(MedicalTest,on_delete=models.PROTECT)
    resultType=models.ForeignKey(ResultType,on_delete=models.PROTECT)

    def __str__(self):
        return ("Result:\n"+"Value: "+str(self.value)+"\n"+str(self.medicalTest)+str(self.resultType))
