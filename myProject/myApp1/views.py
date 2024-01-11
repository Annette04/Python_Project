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
    model2 = AnimatedSkills.objects.all()
    context = {
        'VisualDateSkills': model1,
        'AnimatedSkills': model2
    }
    return render(request, 'skills.html', context)

def lastVac_page(request):
    def getPage(page, params):
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        return data
    def get_array(df):
        headers = list(df.to_dict().keys())
        column1 = df[headers[0]]
        column2 = df[headers[1]]
        res = [headers]
        for i in range(len(column1)):
            l = [column1[i], column2[i]]
            res.append(l)
        return res

    for page in range(0, 1):
        params = {
            'text': 'NAME:Android',
            'per_page': 100
        }
        params1 = {
            'text': 'NAME:Андроид',
            'per_page': 100
        }
        jsObj = json.loads(getPage(page, params))
        jsObj1 = json.loads(getPage(page, params1))
        df = pd.DataFrame(jsObj['items'])
        df1 = pd.DataFrame(jsObj1['items'])
        res = pd.concat([df, df1], join='outer', ignore_index=True).sort_values(by='published_at', ascending=False)
        date = (datetime.datetime.now() - datetime.timedelta(1)).strftime('%Y-%m-%dT%H:%M:%S')
        result = res[res['published_at'] >= date].head(10).reset_index(drop=True)
        if (jsObj['pages'] - page) <= 1:
            break

    a = get_array(result[['name', 'published_at']])
    context = {
        'GetHHVacancies': a
    }
    return render(request, 'lastVac.html', context)

