from django.shortcuts import render, redirect

# Create your views here.
import requests
from datetime import date
from .models import *


def home_view(request):
    tasks = Tasks.objects.all().order_by('-date_added')
    search = ''

    if request.method == 'POST':
        task = request.POST.get('task')
        delete = request.POST.get('delete')

        if task != '' and task != None:
            Tasks.objects.create(text=task)
            return redirect('/')

        if request.POST.get('search') != '':
            search = request.POST.get('search')

        if delete != '' and delete != None:
            Tasks.objects.get(id=delete).delete()
            return redirect('/')

    context = {
        'tasks': tasks,
        'search_result': search
    }

    return render(request, 'home.html', context)


def weather_view(request):
    search_location = ''

    if request.POST.get('search_location') != '':
        search_location = request.POST.get('search_location')
        base_url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={search_location}&units=metric&APPID=f33a484cf794d08d0148764789aaba32').json()
        # print(base_url['weather'][0]['description']) # The way django parses a dictionary (see weather.html -> without [])

    context = {
        'weather_dict': base_url,
        'date': date.today()
    }

    return render(request, 'weather.html', context)


def quiz_view(request):
    print(request.POST)

    context = {
        'correct_answers': 1
    }

    return render(request, 'quiz.html', context)


def flex_view(request):
    return render(request, 'flex.html')


def charts_view(request):
    processors = {
        'AMD': {
            '3700x': 600,
            '3900x': 700
        },
        'Intel': {
            '10700k': 700,
            '10900k': 800
        }
    }

    name = []
    score = []

    for processor, processor_info in processors.items():
        for info in processor_info:
            name.append(processor + ' ' + info)
            score.append(processor_info[info])

    products = {}

    for index, cpu in enumerate(name):
        products[cpu] = score[index]

    x = len(products)

    sorted_name = []
    sorted_score = []

    while len(sorted_name) < x:
        max = -1
        name = ''

        for cpu in products:
            if products[cpu] > max:
                max = products[cpu]
                name = cpu

        sorted_name.append(name)
        sorted_score.append(max)
        products.pop(name)

    context = {
        'sorted_name': sorted_name,
        'sorted_score': sorted_score
    }

    return render(request, 'chart.html', context)
