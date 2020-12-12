from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import *

def index(request):
    latest_analysis_list=Result.objects.all()
    template=loader.get_template('navbar.html')
    context={
        'results':
        latest_analysis_list
        }

    return HttpResponse(template.render(context,request))
