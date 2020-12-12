from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import *
from authentication.models import Patient

def home(request):
    latest_analysis_list=Result.objects.all()
    template=loader.get_template('analysis/home_page.html')
    context={
        'results':
        latest_analysis_list
        }

    return HttpResponse(template.render(context,request))


def add(request):
    template=loader.get_template('analysis/add_entity.html')
    context={}
    return HttpResponse(template.render(context,request))


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


def show_all(request):
    try:
        searched_patient=Patient.objects.get(User_id=request.user.id)
    except Patient.DoesNotExist:
        return HttpResponse("Only patients have tests!")
    #results=Result.objects.all()
    medicalTests=MedicalTest.objects.filter(patient=searched_patient)
    results=Result.objects.filter(pk__in=[x.pk for x in medicalTests])
    template=loader.get_template('analysis/show_all.html')
    context={'results':
        results
        }
    return render(request,'analysis/show_all.html',context)
