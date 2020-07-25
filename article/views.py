from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request, slug):
    page = Article.objects.get(slug=slug)
    context = {
        'page' : page,
    }
    """Отображение страницы Вопросы и ответы"""
    return render(request, 'article/base_page.html', context=context)