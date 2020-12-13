from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import *
from authentication.models import Patient
from .forms import ResultForm


def home(request):
    latest_analysis_list=Result.objects.all()
    template=loader.get_template('analysis/home_page.html')
    context={
        'results':
        latest_analysis_list
        }

    return HttpResponse(template.render(context,request))


def add(request):
    form=ResultForm()
    if request.method=='POST':
        form=ResultForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}

    return render(request,'analysis/add_entity.html',context)


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
        searched_patient=Patient.objects.get(user_id=request.user.id)
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



