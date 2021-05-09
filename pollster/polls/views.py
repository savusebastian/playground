from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import *


def home_view(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'home.html', context)


def detail_view(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    return render(request, 'detail.html', {'question': question})


def results_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'results.html', {'question': question})


def vote_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question': question, 'error_message': 'You did not selected anything.'})

    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('results', args=(question.id,)))
