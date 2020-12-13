from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import *
from authentication.models import Patient
from .forms import *


def home(request):
    latest_analysis_list=Result.objects.all()
    template=loader.get_template('analysis/home_page.html')
    context={
        'results':
        latest_analysis_list
        }

    return HttpResponse(template.render(context,request))


def add(request):
   
    context={}

    return render(request,'analysis/add_entity.html',context)
   
def add_clinic(request):
    form=HealthClinicForm()
    if request.method=='POST':
        form=HealthClinicForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form,'success':False}
    return render(request,'analysis/add_clinic.html',context)

def add_medical_test(request):
    form=MedicalTestForm()
    if request.method=='POST':
        form=MedicalTestForm(request.POST)
        if form.is_valid():
            patient=Patient.objects.get(pk=request.user.pk)
            hc=HealthClinic.objects.get(pk=request.POST['health_clinic'])
            mt=MedicalTest(patient=patient,health_clinic=hc)
            mt.save()

    context={'form':form}
    return render(request,'analysis/add_medical_test.html',context)

def add_result_type(request):
    form=ResultTypeForm()
    if request.method=='POST':
        form=ResultTypeForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'analysis/add_result_type.html',context)

def add_result(request):
    form=ResultForm()
    patient=Patient.objects.get(pk=request.user.pk)
    form.fields["medicalTest"].queryset=MedicalTest.objects.filter(pk=patient.id)
    if request.method=='POST':
        form=ResultForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'analysis/add_result.html',context)

def chat(request):
    template=loader.get_template('analysis/chat.html')
    context={}
    return HttpResponse(template.render(context,request))

def statistics(request):
    template=loader.get_template('analysis/statistics.html')
    context={}
    return HttpResponse(template.render(context,request))

def myprofile(request):
    template=loader.get_template('analysis/my_profile.html')
    context={}
    return HttpResponse(template.render(context,request))

def notifications(request):
    template=loader.get_template('analysis/notifications.html')
    context={}
    return HttpResponse(template.render(context,request))

@login_required
def show_all(request):
    #getting the patient
    try:
        searched_patient=Patient.objects.get(User_id=request.user.id)
    except Patient.DoesNotExist:
    #getting all the medical tests for the pacient
        return render(request, '404_page.html')
    #results=Result.objects.all()
    medicalTests=MedicalTest.objects.filter(patient=searched_patient)

    #getting the clinics where the medical tests from medicalTests had been made
    clinics=[]
    for mt in medicalTests:
        clinic=mt.health_clinic
        if clinic not in clinics:
            clinics.append(clinic)

    #creating a dictionary (key=clinic, value=dictionary(key=mt,value=list(res)))
    dictOfListOfList={}
    for clinic in clinics:
        medicalTestsFilteredByClinics=medicalTests.filter(health_clinic=clinic)
        for mt in medicalTestsFilteredByClinics:
            results=list(Result.objects.filter(medicalTest=mt))
            listOfList=[mt,results]
            dictOfListOfList[clinic]=listOfList
    #results=Result.objects.filter(pk__in=[x.pk for x in medicalTests])
    template=loader.get_template('analysis/show_all.html')
    context={
        'data':
        dictOfListOfList
        }
    return render(request,'analysis/show_all.html',context)
    #return dictOfListOfList


def show_clinics(request):
    d=show_all(request)
    clinics=[]
    for key in d.keys():
        clinics.append(key)
    context={
        'clinics':
        clinics
        }
    return render(request,'analysis/show_all.html',context)



