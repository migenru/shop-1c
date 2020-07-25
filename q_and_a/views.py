from django.shortcuts import render

# Create your views here.

from .models import Question, Answer

def index(request):
    """Отображение вопросов и ответов"""
    questions = Question.objects.all()
    answers = Answer.objects.all()
    return render(request, 'q_and_a/base_index.html', {'questions': questions, 'answers': answers,})
