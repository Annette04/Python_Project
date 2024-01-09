from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from .models import *
# Create your views here.

def index_page(request):
    return render(request, 'index.html')

def importance_page(request):
    model1 = VisualDateImportance.objects.all()
    context = {
        'VisualDateImportance': model1,
    }
    return render(request, 'importance.html', context)

def geography_page(request):
    model1 = VisualDateGeography.objects.all()
    context = {
        'VisualDateGeography': model1,
    }
    return render(request, 'geography.html', context)

def skills_page(request):
    model1 = VisualDateSkills.objects.all()
    context = {
        'VisualDateSkills': model1,
    }
    return render(request, 'skills.html', context)

def lastVac_page(request):
    return render(request, 'lastVac.html')

