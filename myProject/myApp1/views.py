from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request, 'index.html')

def importance_page(request):
    return render(request, 'importance.html')

def geography_page(request):
    return render(request, 'geography.html')

def skills_page(request):
    return render(request, 'skills.html')

def lastVac_page(request):
    return render(request, 'lastVac.html')