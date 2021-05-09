from django.shortcuts import render, redirect
# from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def home_view(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form
    }

    # return HttpResponse('<h1>Home</h1>')
    return render(request, 'home.html', context)


def update_task_view(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'update_task.html', context)


def delete_task_view(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()

        return redirect('/')

    context = {
        'item': item
    }

    return render(request, 'delete.html', context)
