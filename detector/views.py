from django.shortcuts import render
from .models import Article

def index(request):
    article_list = Article.objects.all()
    return render(request, 'detector/index.html', {'article_list': article_list})

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detector/detail.html', {'article': article})
