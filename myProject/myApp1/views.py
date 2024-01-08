from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from .models import VisualDate
# Create your views here.

def index_page(request):
    return render(request, 'index.html')

def importance_page(request):
    model1 = VisualDate.objects.all()
    context = {
        'VisualDate': model1,
    }
    return render(request, 'importance.html', context)

def geography_page(request):
    return render(request, 'geography.html')

def skills_page(request):
    return render(request, 'skills.html')

def lastVac_page(request):
    return render(request, 'lastVac.html')

