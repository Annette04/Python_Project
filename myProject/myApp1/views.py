import datetime
import json
import requests
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from .models import *
import re
# views.py
from django.shortcuts import redirect


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
    url = 'https://api.hh.ru/vacancies'

    def reformate_salary(salary):
        if salary != None and (salary['from'] != None or salary['to'] != None) and salary['currency'] != None:
            if salary['from'] == None:
                return 'до ' + str(salary['to']) + ' ' + salary['currency']
            elif salary['to'] == None:
                return 'от ' + str(salary['from']) + ' ' + salary['currency']
            else:
                return 'от ' + str(salary['from']) + ' до ' + str(salary['to']) + ' ' + salary['currency']
        else:
            return 'Не указан'

    def reformate_skills(skills):
        res = ''
        for dict in skills:
            res += dict['name'] + ', '
        return res[:-2]

    def get_array():
        df = get_all_inf_about_vac()
        df['salary'] = df['salary'].apply(lambda x: reformate_salary(x))
        df['description'] = df['description'].apply(lambda x: re.sub(re.compile('<.*?>'), '', x))
        df['employer'] = df['employer'].apply(lambda x: x['name'])
        df['area'] = df['area'].apply(lambda x: x['name'])
        df['key_skills'] = df['key_skills'].apply(lambda x: reformate_skills(x))
        df['published_at'] = df['published_at'].apply(lambda x: x.replace('T', ' ')[:-5])

        name = df['name'].tolist()
        salary = df['salary'].tolist()
        description = df['description'].tolist()
        employer = df['employer'].tolist()
        area = df['area'].tolist()
        key_skills = df['key_skills'].tolist()
        published_at = df['published_at'].tolist()
        url = df['alternate_url'].tolist()
        res = []
        for i in range(len(name)):
            l = [name[i], salary[i], description[i], employer[i], area[i], key_skills[i], published_at[i], url[i]]
            res.append(l)
        return res

    def getPage(url, params):
        req = requests.get(url, params)
        data = req.content.decode()
        req.close()
        return data

    def made_top_10():
        params = {
            'text': 'NAME:Android',
            'per_page': 50
        }
        params1 = {
            'text': 'NAME:Андроид',
            'per_page': 50
        }
        jsObj = json.loads(getPage(url, params))
        jsObj1 = json.loads(getPage(url, params1))
        df = pd.DataFrame(jsObj['items'])
        df1 = pd.DataFrame(jsObj1['items'])
        res = pd.concat([df, df1], join='outer', ignore_index=True).sort_values(by='published_at', ascending=False)
        date = (datetime.datetime.now() - datetime.timedelta(1)).strftime('%Y-%m-%dT%H:%M:%S')
        top = res[res['published_at'] >= date].head(10).reset_index(drop=True)
        return top

    def get_all_inf_about_vac():
        result = pd.DataFrame()
        top = made_top_10()
        for i in range(top.shape[0]):
            url = top['url'][i]
            req = requests.get(url)
            data = req.content.decode()
            req.close()
            response = json.loads(data)
            superDF = pd.DataFrame.from_dict(response, orient='index')
            superDF = superDF.transpose()[
                ['name', 'salary', 'description', 'employer', 'area', 'key_skills', 'published_at', 'alternate_url']]
            result = pd.concat([result, superDF])
        result = result.reset_index(drop=True)
        return result

    listVac = get_array()
    context = {
        'GetHHVacancies': listVac
    }
    return render(request, 'lastVac.html', context)

def about_page(request):
    model = AboutAuthor.objects.all()
    context = {
        'AboutAuthor': model
    }
    return render(request, 'about.html', context)

def spinner_page(request):
    # response = redirect('lastVac.html')
    # return response
    return render(request, 'spinner.html')
