from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import *

def index(request):
    latest_analysis_list=Result.objects.all()
    context={
        'latest_analysis_list':
        latest_analysis_list
        }

    stringRes=""
    for a in latest_analysis_list:
        stringRes+=str(a)+"\n"


    return HttpResponse(stringRes)
