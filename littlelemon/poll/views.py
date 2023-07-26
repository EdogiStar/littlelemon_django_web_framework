from django.shortcuts import render
from .models import Question
from .models import Choice

# Create your views here.

def homepage(request):
    return render(request, 'poll/index.html')


def detail(request):
    return render(request, 'poll/detail.html')


def display_poll(request):
    questions_data = Question.objects.all()
    main_data = {"questions":questions_data}
    return render(request, 'poll/detail.html', {"questions":main_data})


def display_choices(request):
    choice_data = Choice.objects.all()
    main_data = {"choice":choice_data}
    return render(request, 'poll/index.html', {"choice":main_data})
