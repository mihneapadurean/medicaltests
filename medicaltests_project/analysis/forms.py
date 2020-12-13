from django.forms import ModelForm
from django import forms
from .models import Result,HealthClinic,ResultType,MedicalTest

class HealthClinicForm(ModelForm):
    class Meta:
        model=HealthClinic
        fields='__all__'


class MedicalTestForm(ModelForm):
    class Meta:
        model=MedicalTest
        fields=['health_clinic']

  
class ResultTypeForm(forms.Form):
    type=forms.CharField(label="Type",max_length=200)
    category=forms.CharField(label="Category",max_length=200)
    measurement_type=forms.CharField(label="Measurement Type",max_length=200)

class ResultForm(ModelForm):
    class Meta:
        model=Result
        fields='__all__'
    
