from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import *

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
    template=loader.get_template('analysis/show_all.html')
    context={}
    return HttpResponse(template.render(context,request))