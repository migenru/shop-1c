from django.shortcuts import render

# Create your views here.

from .models import Question, Answer

def index(request):
    """Отображение вопросов и ответов"""
    questions = Question.objects.all()
    return render(request, 'q_and_a/q_and_a_index.html', {'questions': questions,})
